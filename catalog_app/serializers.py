from catalog_app.models import Category, Good
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'comment', 'is_mark', 'created', 'updated']


class GoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Good
        fields = ['name', 'comment', 'is_mark', 'created', 'updated', 'category']
