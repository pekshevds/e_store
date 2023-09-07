from django.urls import path
from django.urls import include

from rest_framework import routers
from rest_app.views import GoodViewSet
from rest_app.views import CategoryViewSet
from rest_app.views import OrderViewSet
from rest_app.views import UserViewSet

router = routers.DefaultRouter()
router.register('goods', GoodViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
