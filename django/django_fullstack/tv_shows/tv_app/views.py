from django.shortcuts import render , redirect , HttpResponse
from . import models 

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
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        models.create_show(title= title, network=network , release_date=release_date,description=description)
        return redirect('/shows')
    else:
        return HttpResponse('Error : Wrong Info')

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
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']
    models.update_show(id=id , title = title , network=network , release_date=release_date , description=description)
    return redirect('/shows')

def delete( request ,id):
    models.delete_show(id=id)
    return redirect('/shows')