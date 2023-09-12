"""
URL configuration for e_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('index_app.urls', 'index'))),
    path('admin/', admin.site.urls),
    path('auth/', include(('auth_app.urls', 'auth'))),
    path('api/', include(('rest_app.urls', 'api'))),
    path('catalog/', include(('catalog_app.urls', 'catalog'))),
    path('cart/', include(('cart_app.urls', 'cart'))),
    path('wish/', include(('wish_app.urls', 'wish'))),
    path('order/', include(('order_app.urls', 'order'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
