from django.shortcuts import render , redirect
from .models import user
def index(request):
    context = {
        'all_users' : user.objects.all(),
    }
    return render(request,'index.html',context)

def create_user(request):
    first = request.POST['first_name']
    last = request.POST['last_name']
    mail = request.POST['email']
    old = request.POST['age']
    user.objects.create(first_name = first , last_name = last , email_address = mail , age = old)
    return redirect('/')
