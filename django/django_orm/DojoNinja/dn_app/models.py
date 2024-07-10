from django.db import models

class dojo(models.Model):
    name = models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ninja(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dojo = models.ForeignKey(dojo , related_name='ninjas', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def view_dojo():
    return dojo.objects.all()

def create_dojo(name , city , state):
    return dojo.objects.create(name = name , city = city , state = state )

def create_ninja(first_name , last_name , id):
    the_dojo = dojo.objects.get(id=id)
    return ninja.objects.create(first_name = first_name , last_name= last_name , dojo = the_dojo )

def delete_dojo(id):
    the_dojo = dojo.objects.get(id=id)
    return the_dojo.delete()