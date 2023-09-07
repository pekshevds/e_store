from rest_framework import viewsets
from rest_framework import permissions

from catalog_app.models import Good
from catalog_app.models import Category
from order_app.models import Order
from auth_app.models import User

from rest_app.serializers import GoodSerializer
from rest_app.serializers import CategorySerializer
from rest_app.serializers import OrderSerializer
from rest_app.serializers import UserSerializer


class GoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Goods to be viewed or edited.
    """
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
