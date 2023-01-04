from api.actions.auth import UserBasicAuthView
from api.actions.order import CreateOrderView
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("order", CreateOrderView.as_view(), name="create_order"),
    path("auth/signup", UserBasicAuthView.as_view(), name="register"),
    path(
        "auth/signin", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify", TokenVerifyView.as_view(), name="token_verify"),
]
