from rest_framework import serializers
from decimal import Decimal
from .models import Menu,Booking
from django.contrib.auth.models import User,Group,GroupManager

class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model= Menu
        fields = ['id','f_name','f_price', 'f_inventory']
    #despues de esto se declaran las vistas de MenuItmeView y SingleMenuItemView
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields ='__all__'
class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']