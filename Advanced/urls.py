from django.contrib import admin
from django.urls import path
from Advanced import views


urlpatterns = [
    path('', views.advanced, name='advanced'),
    path('eightFift', views.eightFift, name='eightFift'),
    path('eightMoreFift', views.eightMoreFift, name='eightMoreFift'),
    path('fifteen', views.fifteen, name='fifteen'),
    path('fifteenFive', views.fifteenFive, name='fifteenFive'),
    path('five', views.five, name='five'),
    path('fiveTen', views.fiveTen, name='fiveTen'),
    path('ten', views.ten, name='ten'),

]
