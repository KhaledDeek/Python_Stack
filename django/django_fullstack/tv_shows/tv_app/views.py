from django.shortcuts import render , redirect , HttpResponse
from . import models 
from django.contrib import messages
from django.http import JsonResponse
def pre_show(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': models.all_shows()
    }
    return render(request , 'shows.html', context)


def new_show(request):
    return render(request , 'new_show.html')

def create_show(request):
    if request.method == 'POST':
        errors = models.show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request, value)
            return redirect('/shows/create_show')
        else: 
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description'] 
            models.create_show(title= title, network=network , release_date=release_date,description=description)
            messages.success(request, "Show successfully created")
            return redirect('/shows')
    else:
        return render(request , 'new_show.html')


def show_info(request , id):
    context = {
        'show':models.show_info(id=id)
    }
    return render(request ,  'show_info.html' , context )


def edit_show(request , id):
    context = {
        'show':models.show_info(id=id)
    }
    return render(request,'edit_show.html',context)

def update_show(request , id):
    if request.method == 'POST':
        errors = models.show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request, value)
            return redirect('edit_page' , id)
        else: 
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']
            models.update_show(id=id , title = title , network=network , release_date=release_date , description=description)
            messages.success(request, "Show successfully updated")
            return redirect('/shows')
    else:
        return render(request , 'edit_show.html')

def delete( request ,id):
    models.delete_show(id=id)
    return redirect('/shows')