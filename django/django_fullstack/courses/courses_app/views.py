from django.shortcuts import render , redirect
from . import models
from django.contrib import messages

def index(request):
    context = {
        'courses' : models.view_courses() 
    }
    return render(request , 'index.html', context)

def create_course(request):
    if request.method == 'POST':
        errors = models.Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            name = request.POST['name']
            description = request.POST['text_area']
            models.create_course(name = name , description=description)
            return redirect('/')


def view_course(request , id):
    context = {
        'thecourse': models.view_course_info(id=id)
    }
    return render(request , 'delete.html', context)

def destroy_course(request , id):
    models.destroy_course(id=id)
    return redirect('/')

def view_comments(request , id ):
    context = {
        'course' : models.view_course_info(id =id)
    }
    return render( request , 'comments.html' , context)


def create_comment(request , id):
    models.create_comment(id=id , com = request.POST['txtarea'] )
    return redirect('comments' , id)

