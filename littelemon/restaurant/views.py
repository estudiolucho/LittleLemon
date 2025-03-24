from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.viewsets   import ModelViewSet
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer,UserSerializer
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView (generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated] #solo  permite con usuarios autenticados TOKEN
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    print(serializer_class)
    #despues se definen las ritas en urls.py de aplicacion
class SingleMenuItemView(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class BookingViewSet (ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]
    
class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]