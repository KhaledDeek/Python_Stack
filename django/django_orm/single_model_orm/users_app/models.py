from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




def view_users():
    return user.objects.all()

def create_user(first_name , last_name , email_address , age):
    return user.objects.create(first_name = first_name , last_name = last_name , email_address = email_address , age = age )