from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process' , views.process_money),
    path('checkout', views.checkout),
    path('clear' , views.delete_session)
]
