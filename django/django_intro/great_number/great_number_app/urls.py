from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.rand),
    path('game' , views.index),
    path('num' , views.num),
    path('winners' , views.winners),
    path('reset' , views.reset)
]