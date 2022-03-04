from django.db import models

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