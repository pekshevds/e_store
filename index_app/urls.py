from django.urls import path
from django.urls import include
from index_app.views import index

from rest_framework import routers
from index_app.views import GoodViewSet
from index_app.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('goods', GoodViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', index),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
