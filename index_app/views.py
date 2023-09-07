from django.shortcuts import render, HttpResponse

from rest_framework import viewsets
from rest_framework import permissions

from catalog_app.models import Good
from catalog_app.models import Category

from catalog_app.serializers import GoodSerializer
from catalog_app.serializers import CategorySerializer


def index(request) -> HttpResponse:
    return render(request, "index_app/index.html")


class GoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Goods to be viewed or edited.
    """
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
