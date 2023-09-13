from django.urls import path
from cart_app.views import Index


app_name = "cart"
urlpatterns = [
    path('', Index.as_view(), name="index-page"),
    path('add/<int:good_id>/', Index.add),
]
