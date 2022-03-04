from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Region(models.Model):
    name = models.CharField(max_length=200)
    localization = models.CharField(max_length=400)
    capital = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=200)
    loc = models.CharField(max_length=400)
    

    def __str__(self):
        return self.name

class Land(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=400)
    capital = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Race(models.Model):
    name = models.CharField(max_length=300)
    land = models.ForeignKey(Land,on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Hero(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=300)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Messagge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:60]

