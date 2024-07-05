from django.shortcuts import render , redirect
from . import models
def index(request):
    context = {
        'all_users' : models.view_users(),
    }
    return render(request,'index.html',context)

def create_user(request):
    first = request.POST['first_name']
    last = request.POST['last_name']
    mail = request.POST['email']
    old = request.POST['age']
    models.create_user(first , last , mail , old)
    return redirect('/')
