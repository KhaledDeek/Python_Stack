from django.db import models
import re
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def signup_validator(self , postData):
        errors = {}
        if len(postData['name']) < 2 : 
            errors['name'] = 'Name must be at least 2 characters '
        if len(postData['alias']) < 2 : 
            errors['alias'] = 'Alias must be at least 2 characters '
        if len(postData['password']) < 8 : 
            errors['password'] = 'Password should be at least 8 characters'
        if postData['password'] != postData['confirmPassword'] :
            errors['cpw'] = 'Passwords do not match'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already exists"
        return errors
    def login_validator(self , postData):
        warnings = {}
        if postData['email'] == '':
            warnings['email'] = 'Email field cant be empty'
        elif postData['password'] == '':
            warnings['password'] = 'Password field cant be empty'
        else:
            if User.objects.filter(email = postData['email']).exists() == False : 
                warnings['email'] = "Email does not exist"
            if bcrypt.checkpw(postData['password'].encode(), view_user(email = postData['email']).password.encode()) == False :
                warnings['password'] = 'Incorrect Password'
        return warnings




class User(models.Model):
    name = models.CharField(max_length=50)
    alias    = models.CharField(max_length= 50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author , related_name='books' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Review(models.Model):
    review = models.TextField()
    users = models.ForeignKey(User , related_name='reviews' , on_delete=models.CASCADE)
    books = models.ForeignKey(Book , related_name='reviews' , on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def create_user(name , alias , email , password ):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(name = name , alias = alias , email = email , password = pw_hash)

def view_user(email):
    user = User.objects.get(email = email)
    return user
def user_info(id):
    user =User.objects.get(id=id)
    return user

def view_book(id):
    return Book.objects.get(id = id)

def all_books():
    return Book.objects.all()

def all_authors():
    return Author.objects.all() 

def create_author(name):
    return Author.objects.create(name = name)

def create_book(postData):
    if postData['select_author'] == 'Select Author':
        return Book.objects.create(title = postData['title'] , author = Author.objects.create(name = postData['new_author']) )
    
    else:
        return Book.objects.create(title = postData['title'] , author = Author.objects.get(name = postData['select_author']) )


def create_review(postData , user , book ):
    return Review.objects.create(review = postData['review'] ,rating = postData['rating'] , users = user , books = book)

def delete_review( id):
    review = Review.objects.get(id = id)
    return review.delete()

def all_reviews():
    return Review.objects.all