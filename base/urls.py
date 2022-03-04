from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('race/<str:pk>/',views.race, name="race"),
    path('land/<str:pk>/',views.land, name="land"),
]