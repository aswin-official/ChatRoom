from django import views
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
]