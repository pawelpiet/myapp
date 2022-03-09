from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('',views.home, name="home"),
    path('race/<str:pk>/',views.race, name="race"),
    path('land/<str:pk>/',views.land, name="land"),
    path('hero/<str:pk>/',views.hero, name="hero"),
    path('room/<str:pk>/',views.room, name="room"),

    path('create-room/',views.createRoom, name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom, name="delete-room"),
]