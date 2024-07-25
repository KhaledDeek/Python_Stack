from django.shortcuts import render , redirect
from . import models
from django.contrib import messages
import bcrypt

def main(request):
    return render(request ,'main_page.html')



def register(request):
    if request.method == 'POST':
        errors = models.User.objects.signup_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request , value)
            return redirect('/')
        else:
            new_user = models.create_user(name=request.POST['name'] , alias=request.POST['alias'] , email=request.POST['email'] , password=request.POST['password'] )
            request.session['email'] = request.POST['email']
            request.session['id'] = new_user.id
            return redirect('/books')
    else:
        return redirect('/')


def validate_login(request):
    if request.method == 'POST':
        warnings = models.User.objects.login_validator(request.POST)
        if warnings:
            for k , value in warnings.items():
                messages.warning(request , value)
            return redirect('/')
        else:
            user = models.view_user(email=request.POST['email'])
            request.session['email'] = user.email
            request.session['id'] = user.id
        return redirect('/books')
        
    else:
        return redirect('/')

def books(request):
    context = {
        'user' : models.view_user(email = request.session['email'] ),
        'books': models.all_books(),
        'reviews':models.all_reviews()
        }
    return render(request , 'books.html' , context)

def create_book(request):
    context = {
        'authors':models.all_authors()
    }
    return render(request , 'create_book.html',context)

def new_book(request):
    book = models.create_book(postData=request.POST)
    review = models.create_review(postData=request.POST , user = models.user_info(id = request.session['id']) , book = book)
    return redirect('/book_info/'+str(book.id))

def book_info(request , id):
    context = {
        'book' : models.view_book(id = id),
    }
    request.session['book_id'] = id
    return render(request,'book_info.html', context)

def create_review(request , id):
    models.create_review(postData=request.POST , user = models.view_user(email = request.session['email']) , book = models.view_book(id=id))
    return redirect('/book_info/'+str(id))

def delete_review(request ,id):
    models.delete_review(id = id)
    return redirect('/book_info/'+str(request.session['book_id']))  

def user_info(request , id):
    context = {
        'user':models.user_info(id=id)
    }
    return render(request ,'user_info.html',context )

def logout(request):
    request.session.clear()
    return redirect('/')