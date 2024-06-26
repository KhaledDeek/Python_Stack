from django.shortcuts import render , redirect

def index(request):
    if 'count' not in request.session: 
        request.session['count'] = 0
    request.session['count'] +=1
    if 'visits' not in request.session: 
        request.session['visits'] = 0
    request.session['visits'] +=1
    if 'counter' not in request.session:
        request.session['counter'] = 1
    context = {
        "sum" : request.session['count'] ,
        "visits" : request.session['visits'] , 
        "counter" : request.session['counter']
    }
    return render(request , 'index.html' , context)


def delete(request):
    del request.session['count']    
    del request.session['visits']
    request.session['count'] = 0
    request.session['visits'] = 0
    return redirect('/')

def inc2(request):
    request.session['count'] +=1
    request.session['counter'] = 2
    return redirect('/')

def increment(request):
    request.session['number'] = request.POST['number'] 
    request.session['count'] += (int(request.session['number']) -1 )
    request.session['counter'] = request.session['number']
    return redirect('/')