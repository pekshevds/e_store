from rest_framework import viewsets
from rest_framework import permissions

from catalog_app.models import Good
from catalog_app.models import Category
from order_app.models import Order
from order_app.models import OrderItem
from auth_app.models import User
from cart_app.models import CartItem
from wish_app.models import WishItem

from rest_app.serializers import GoodSerializer
from rest_app.serializers import CategorySerializer
from rest_app.serializers import OrderSerializer
from rest_app.serializers import OrderItemSerializer
from rest_app.serializers import UserSerializer
from rest_app.serializers import CartItemSerializer
from rest_app.serializers import WishItemSerializer


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


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Order items to be viewed or edited.
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cart items to be viewed or edited.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAdminUser]


class WishItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cart items to be viewed or edited.
    """
    queryset = WishItem.objects.all()
    serializer_class = WishItemSerializer
    permission_classes = [permissions.IsAdminUser]
