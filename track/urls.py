from django.contrib import admin
from django.urls import path
from track import views


urlpatterns = [
    path('', views.track, name='track'),
    path('mens', views.mens, name='mens'),
    path('womens', views.womens, name='womens'),
]