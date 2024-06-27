from django.shortcuts import render , HttpResponse

def user(request):
    return HttpResponse('Hello User')

def register(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to log in')

def list(request):
    return HttpResponse('placeholder to later display all the list of users')