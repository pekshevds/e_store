from django.urls import path
from wish_app.views import Index


app_name = "wish"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
]
