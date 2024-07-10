from django.shortcuts import render , redirect
from . import models
def index(request):
    context = {
        'books' : models.view_books() 
    }
    return render(request , 'book.html' , context)

def desc(request , id):
    book = id
    context = {
        'details': models.book_info(id=book),
        'authors' : models.filter_author(id=book)
    }
    return render(request , 'book_info.html',context )

def create_book(request):
    title = request.POST['title']
    desc = request.POST['description']
    models.create_book(title=title , desc=desc)
    return redirect('/')


def author(request):
    context = {
        'authors' : models.view_authors()
    }
    return render (request , 'author.html', context)

def create_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['note']
    models.create_author(first_name = first_name , last_name = last_name , notes = notes)
    return redirect('/author')

def add_author(request , id ):
    selected= request.POST['selected']
    models.add_author(id=id ,selected=selected)
    return redirect("/")


def info(request, id):
    author = id
    context = {
        'author_details': models.author_info(id=author),
        'books' : models.view_books() 
    }
    return render(request , 'author_info.html',context )

def add_book(request , id ):
    selected= request.POST['selected']
    models.add_book(id=id ,selected=selected)
    return redirect('/author')
