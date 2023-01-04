from api.actions.auth.serializers import (UserAuthResponseSerializer,
                                          UserBasicAuthSerializer)
from api.models.user import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, response, status
from rest_framework_simplejwt.tokens import RefreshToken


class UserBasicAuthView(generics.GenericAPIView):
    serializer_class = UserBasicAuthSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: UserAuthResponseSerializer()}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        refresh = RefreshToken.for_user(user)
        return response.Response(
            {"refresh": str(refresh), "access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )
