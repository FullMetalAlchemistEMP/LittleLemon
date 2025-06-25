from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import viewsets 
from rest_framework import permissions

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated] 