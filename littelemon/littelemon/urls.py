"""
URL configuration for littelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from restaurant import views
router=routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet) #habilita http://127.0.0.1:8000/restaurant/booking/tables
router.register(r'users', views.UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/',include('restaurant.urls')),
    path('restaurant/menu/',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    #url para djoser
    path('auth/', include('djoser.urls')),#habilita http://127.0.0.1:8000/auth/token/login/ y #habilita http://127.0.0.1:8000/auth/token/logout
    path('auth/', include('djoser.urls.authtoken'))
    # token para manager1 93d7038f094875b8dcab6cfe3021c6df327a6949


]
