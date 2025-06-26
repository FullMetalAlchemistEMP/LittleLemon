from django.contrib import admin 
from django.urls import path 
from . import views 

  
urlpatterns = [
    # HTML views
    path('', views.home, name="home"),

    # REST API views
    path('items/', views.MenuItemsView.as_view(), name="api-menu"),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name="api-single-menu"),
]