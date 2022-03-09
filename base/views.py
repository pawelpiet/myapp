from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Land, Race, Hero, Room, User
from .forms import RoomForm
# Create your views here.


def loginPage(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'User or password does not exist')

    context = {}
    return render(request,'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')



def home(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(host__username__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    lands = Land.objects.all()
    users = User.objects.all()
    room_count = rooms.count()
    context = {'lands': lands, 'rooms': rooms, 'users': users, 'room_count': room_count}
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
    return render(request,'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context={'form': form}
    return render(request,'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request,'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj': room})



