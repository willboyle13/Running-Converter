from django.contrib import admin
from django.urls import path
from Pace import views


urlpatterns = [
    path('', views.pace, name='pace'),
    path('calculatepace', views.calculatepace, name='calculatepace'),
    path('calculatesplits', views.calculatesplits, name='calculatesplits'),
]