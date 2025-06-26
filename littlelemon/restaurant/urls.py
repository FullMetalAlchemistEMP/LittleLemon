from django.contrib import admin 
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [
    # HTML views
    path('', views.home, name="home"),

    # REST API views
    path('items/', views.MenuItemsView.as_view(), name="api-menu"),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name="api-single-menu"),
    path('api-token-auth/', obtain_auth_token),
]