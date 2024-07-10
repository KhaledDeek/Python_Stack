from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index),
    path('book/<int:id>' , views.desc),
    path('create_book', views.create_book),
    path('author', views.author),
    path('create_author', views.create_author),
    path('add_author/<int:id>', views.add_author , name="add_author"),
    path('author/<int:id>' , views.info),
    path('add_book/<int:id>', views.add_book),
]