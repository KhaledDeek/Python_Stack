from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.main),
    path('register' , views.register),
    path('login' , views.validate_login),
    path('books' , views.books),
    path('books/add' , views.create_book),
    path('new_book' , views.new_book),
    path('book_info/<int:id>' , views.book_info),
    path('new_review/<int:id>' , views.create_review),
    path('delete_review/<int:id>' , views.delete_review ),
    path("users/<int:id>" , views.user_info),
    path('logout' , views.logout)
]