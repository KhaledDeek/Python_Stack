from django.db import models
from django.contrib import messages
import datetime
import re

class showManager(models.Manager):
    def basic_validator(self , postData):
        errors = {}
        if re.search(postData['title'], postData['title']) != None :
            errors['title'] = 'Title already exists'
        if len(postData['title']) < 2:
            errors['title'] = 'Title should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network name should be at least 3 characters'
        if 0 < len(postData['description']) < 10:
            errors['description'] = 'Description should be at least 10 chracters '
        if postData['release_date']>= datetime.datetime.today().strftime('%Y-%m-%d'):
            errors['release_date'] = 'Release Date should be in the past '
        if 10 > len(postData['release_date']):
            errors['release_date'] = 'Release Date should be at least 10 chracters '
        return errors





class show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=30)
    release_date = models.DateField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = showManager()


def all_shows():
    return show.objects.all()

def create_show(title , network , release_date ,description):
    return show.objects.create(title= title, network=network , release_date=release_date,description=description)

def show_info(id):
    return show.objects.get(id=id)

def update_show(id , title , network , release_date , description ):
    the_show = show.objects.get(id=id)
    the_show.title = title
    the_show.network = network
    the_show.release_date = release_date
    the_show.description = description
    return the_show.save()

def delete_show(id):
    the_show = show.objects.get(id=id)
    return the_show.delete()