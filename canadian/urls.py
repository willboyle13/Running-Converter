from django.contrib import admin
from django.urls import path
from canadian import views


urlpatterns = [
    path('', views.canadian, name='canadian'),
]