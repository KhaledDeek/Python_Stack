from django.db import models

class show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=30)
    release_date = models.DateField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


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