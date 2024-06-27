from django.shortcuts import render , HttpResponse

def display(request):
    return HttpResponse("placeholder to display all the surveys created")

def show(request):
    return HttpResponse("placeholder for users to add a new survey")