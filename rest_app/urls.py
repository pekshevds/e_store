from django.urls import path
from django.urls import include

from rest_framework import routers
from rest_app.views import GoodViewSet
from rest_app.views import CategoryViewSet
from rest_app.views import OrderViewSet
from rest_app.views import OrderItemViewSet
from rest_app.views import UserViewSet
from rest_app.views import CartItemViewSet
from rest_app.views import WishItemViewSet


router = routers.DefaultRouter()
router.register('goods', GoodViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('users', UserViewSet)
router.register('cart', CartItemViewSet)
router.register('wish', WishItemViewSet)


app_name = "api"
urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
