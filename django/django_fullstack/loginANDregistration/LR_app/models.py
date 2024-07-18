from django.db import models
import re
import bcrypt
from datetime import datetime


class UserManager(models.Manager):
    def signup_validator(self , postData):
        errors = {}
        if postData['dob'] == '':
            errors['dob'] = 'Please enter Date of Birth'
        else:
            dob = datetime.strptime(postData['dob'] , "%Y-%m-%d")
            age = int(datetime.today().strftime('%Y')) - int(dob.strftime('%Y')) 
            if age <= 13 : 
                errors['dob'] = 'Age must be greater than 13'
        if len(postData['first_name']) < 2 : 
            errors['first_name'] = 'First Name must be at least 2 characters '
        if len(postData['last_name']) < 2 : 
            errors['last_name'] = 'Last Name must be at least 2 characters '
        if len(postData['password']) < 8 : 
            errors['password'] = 'Password should be at least 8 characters'
        if postData['dob']>= datetime.today().strftime('%Y-%m-%d'):
            errors['dob'] = 'Date of Birth must be in the past'
        if postData['password'] != postData['confirmPassword'] :
            errors['cpw'] = 'Passwords do not match'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = "Invalid email address!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def create_user(first_name , last_name , email , password , dob):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name = first_name , last_name = last_name , email = email , password = pw_hash , dob = dob)



