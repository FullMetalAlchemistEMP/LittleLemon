from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# class BookingViewSet(viewsets.ModelViewSet):
#    queryset = Booking.objects.all()
#    serializer_class = BookingSerializer
#    permission_classes = [permissions.IsAuthenticated] 