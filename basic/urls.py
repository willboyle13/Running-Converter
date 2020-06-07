from django.contrib import admin
from django.urls import path
from basic import views


urlpatterns = [
    path('', views.basic, name='basic'),
    path('distance', views.distance, name='distance'),
    path('sprint', views.sprint, name='sprint'),
]