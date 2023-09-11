from django.urls import path
from index_app.views import Index


app_name = "index"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
]
