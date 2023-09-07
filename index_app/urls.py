from django.urls import path
from django.urls import include
from index_app.views import Index

urlpatterns = [
    path('', Index.as_view()),
    path('api/', include('rest_app.urls')),
]
