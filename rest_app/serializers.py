from rest_framework import serializers

from catalog_app.models import Category
from catalog_app.models import Good

from order_app.models import Order
from order_app.models import OrderItem

from auth_app.models import User

from cart_app.models import CartItem

from wish_app.models import WishItem


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'comment', 'is_mark', 'created', 'updated']


class GoodSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Good
        fields = ['id', 'name', 'comment', 'is_mark', 'created', 'updated', 'category']


class OrderItemSerializer(serializers.ModelSerializer):
    # good = GoodSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order', 'good', 'qnt', 'price', 'amount']


class OrderSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'date', 'comment', 'is_mark', 'created',
                  'updated', 'amount', 'status', 'customer']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

    def create(self, validated_data):
        user = User(username=validated_data['username'], is_superuser=False,
                    email=validated_data['username'] + "@mail.ru",
                    is_stuff=False)
        user.set_password("QWEqwe123")
        user.save()
        return user


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['customer', 'good', 'qnt']


class WishItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishItem
        fields = ['customer', 'good']
