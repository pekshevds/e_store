from django.urls import path
from django.urls import include
from index_app.views import Index


app_name = "index"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
]
