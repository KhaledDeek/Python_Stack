from django.shortcuts import render , redirect
from . import models
def index(request):
    context = {
        'dojos': models.view_dojo()
    }
    return render(request, 'index.html',context)

def create_dojo(request):
    models.create_dojo(name = request.POST['name'] , city  = request.POST['city'] , state = request.POST['state'])
    return redirect('/')

def create_ninja(request):
    models.create_ninja(first_name=request.POST['first_name'], last_name= request.POST['last_name'] , id = request.POST['dojo'])
    return redirect('/')


def delete(request ):
    models.delete_dojo(request.POST['dojo_id'])
    return redirect('/')