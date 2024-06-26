from django.shortcuts import render , HttpResponse
def index(request):
    return render(request , 'index.html')
def view(request):
    name = request.POST['name'],
    location = request.POST['location'],
    language = request.POST['language'],
    text = request.POST['textarea']
    
    context = {
        "name_on_template" : name , 
        "selected_location" : location , 
        "selected_language" : language , 
        "commented": text
        
    }
    return render(request , 'view.html' , context)
