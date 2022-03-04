from django.shortcuts import render
from django.http import HttpResponse
from .models import Land
# Create your views here.

# races = [
#     {'id': 1, 'name': 'Elves'},
#     {'id': 2, 'name': 'Men'},
#     {'id': 3, 'name': 'Dwarves'},
#     {'id': 4, 'name': 'Hobbits'},
#     {'id': 5, 'name': 'Ents'},
#     {'id': 6, 'name': 'Orcs'},
#     {'id': 7, 'name': 'Trolls'},
#     {'id': 8, 'name': 'Spirits'},
#     {'id': 9, 'name': 'Unknowns'},
# ]


def home(request):
    lands = Land.objects.all()
    print('dsd')
    context = {'lands': lands}
    return render(request,'base/home.html', context) 

def race(request,pk):
    race = None
    for i in races:
        if i['id'] == int(pk):
            room = i
    context = {'race':race}
    return render(request,'base/race.html', context)

def land(request,pk):
    land = Land.objects.get(id=pk)
    context = {'land':land}
    return render(request,'base/land.html', context)





