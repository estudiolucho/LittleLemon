from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
        path('', views.index, name='index'),
        #API
        path('menu/', views.MenuItemsView.as_view()),
        path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
        #despues se incluye el en urls.py del proyecto
        path('api-token-auth/',obtain_auth_token) #habilita (POST)http://localhost:8000/restaurant/api-token-auth/ + body(user,pass)
        
        
]