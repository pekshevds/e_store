from django.urls import path
from order_app.views import Index


app_name = "order"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
]
