from django.shortcuts import render
from django.http import HttpResponse
from .models import Land, Race, Hero, Room
# Create your views here.




def home(request):
    lands = Land.objects.all()
    rooms = Room.objects.all()
    print('dsd')
    context = {'lands': lands, 'rooms': rooms}
    return render(request,'base/home.html', context) 

def race(request,pk):
    race = Race.objects.get(id=pk)
    context = {'race':race}
    return render(request,'base/race.html', context)

def land(request,pk):
    land = Land.objects.get(id=pk)
    context = {'land':land}
    return render(request,'base/land.html', context)

def hero(request,pk):
    hero = Hero.objects.get(id=pk)
    context = {'hero':hero}
    return render(request,'base/hero.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/hero.html', context)





