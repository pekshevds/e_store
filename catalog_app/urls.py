from django.urls import path
from catalog_app.views import Index


app_name = "catalog"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
]
