from django.db import models


class author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class book(models.Model):
    author = models.ManyToManyField(author , related_name = 'books' )
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def view_books():
    return book.objects.all()

def view_authors():
    return author.objects.all()

def create_book(title , desc):
    return book.objects.create(title=title , desc=desc )

def create_author(first_name , last_name , notes):
    return author.objects.create(first_name = first_name , last_name = last_name , notes = notes)

def book_info(id):
    return book.objects.get(id=id)

def author_info(id):
    return author.objects.get(id=id)


def filter_author(id):
    thebook = book.objects.get(id=id)
    x = thebook.author.all().values('id')
    return author.objects.all()

def add_author(id , selected):
    thebook = book.objects.get(id=id)
    theauthor = author.objects.get(id=selected)
    return thebook.author.add(theauthor)


def add_book(id , selected):
    theauthor = author.objects.get(id=id)
    thebook = book.objects.get(id=selected)
    return theauthor.books.add(thebook)


