import json
import logging

from api.actions.order.serializers import (CreateOrderSerializer,
                                           ShowOrderSerializer)
from api.models import Check, Order, Printer, User
from api.tasks import render_template
from api.utils import cache
from django.db.models import Max
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

LOGGER = logging.getLogger("root")


def user_same_request(request):
    hash_key = str(hash(request.user.email))
    hash_value = cache.get(hash_key)
    request_hash = str(hash(json.dumps(request.data)))
    cache.set(hash_key, request_hash, ex=6)
    if hash_value and request_hash == hash_value.decode():
        return True
    else:
        return False


def get_last_order(user):
    orders = Order.objects.filter(
        user=user, id=Order.objects.aggregate(Max("id"))["id__max"]
    )
    if not orders:
        return {}

    serializer = ShowOrderSerializer(orders[0])
    return serializer.data


def get_orders(user: User) -> list:
    orders = Order.objects.filter(user=user)
    if not orders:
        return []
    serializer = ShowOrderSerializer(orders, many=True)
    return serializer.data


class CreateOrderView(generics.GenericAPIView):
    # class CreateOrderView(views.APIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ShowOrderSerializer(),
            status.HTTP_409_CONFLICT: ShowOrderSerializer(),
        }
    )
    def post(self, request, *args, **kwargs):
        # я не зовсім зрозумів в який момент замість друку треба повертати інформацю про замовлення
        # так як для подібноі операціі в житті був би колбєк від системи оплати, якщо кліент оплатив то робимо роботу
        # а тут просто працюе блок одного і того ж самого замовлення він одного і того ж самого юзера за період в кілька секунд

        if user_same_request(request):
            order = get_last_order(request.user)
            return Response(order, status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        point_id = validated_data["point_id"]
        LOGGER.info(f"point_id: #{point_id}")

        printers = Printer.objects.filter(point_id=point_id)
        if not printers:
            return Response(
                {"detail": f"Point #{point_id} has no printer"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        order = Order.objects.create(
            user=request.user, point_id=point_id, items=validated_data["order"]
        )
        order.save()

        for printer in printers:
            check = Check.objects.create(
                printer=printer,
                order=order,
                type=printer.check_type,
                status=Check.STATUSES.NEW,
            )
            context = {
                "type": check.type,
                "check_id": check.id,
                "user_id": check.order.user.id,
                "point_id": printer.point_id,
                "order_id": check.order.id,
                "items": [dict(x) for x in check.order.items],
            }
            # Add Task to Celery
            render_template.delay(context)

        order_serializer = ShowOrderSerializer(order)

        return Response(order_serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ShowOrderSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        data = get_orders(request.user)
        return Response(data, status=status.HTTP_200_OK)
