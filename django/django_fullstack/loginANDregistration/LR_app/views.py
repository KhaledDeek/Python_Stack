from django.shortcuts import render , redirect , HttpResponse
from . import models
from django.contrib import messages
import bcrypt

def index(request):
    return render(request , 'index.html')

def register(request):
    if request.method == 'POST':
        errors = models.User.objects.signup_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request , value)
            return redirect('/')
        else:
            models.create_user(first_name=request.POST['first_name'] , last_name=request.POST['last_name'] , email=request.POST['email'] , password=request.POST['password'] , dob = request.POST['dob'])
            request.session['first_name'] = request.POST['first_name']
            return redirect('/success')


def success(request):
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        id = request.session['id']
        context = {
            'fn' : request.session['first_name'] ,
        }
        return render(request , 'welcome.html' , context)



def logout(request):
    del request.session['first_name']
    return redirect('/')

def validate_login(request):
    user = models.User.objects.get(email=request.POST['email'])  
    request.session['first_name'] = user.first_name
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        return redirect('/success')
    else:
        context = {
            'error' : 'Email or Password do not Match'
        }
        return render(request , 'index.html' , context)
