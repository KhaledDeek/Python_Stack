from django.shortcuts import render , redirect

import random 
	

def rand(request):
    request.session['rand'] = random.randint(1, 100) 
    return redirect('/game')
def index(request):
    if 'count' not in request.session:
        request.session['count'] = -1
    request.session['count'] +=1
    if 'number' not in request.session:
        odd = 0
    elif int(request.session['number']) > int(request.session['rand']) : 
        odd = 1
    elif int(request.session['number']) < int(request.session['rand']) : 
        odd = 2
    elif int(request.session['number']) == int(request.session['rand']) : 
        odd = 3
    if int(request.session['count']) > 5 :
        odd = 4
    context = {
        "count" : request.session['count'],
        "rand" : request.session['rand'], 
        "odd" : odd
    }
    return render(request , 'index.html' , context )

def num(request):
    request.session['number'] = request.POST['number']
    return redirect('/game')

def reset(request):
    del request.session['count']
    del request.session['rand']
    del request.session['number']
    return redirect('/')

def winners(request):
    context = {
        "username" : request.POST['users'],
        "attempts" : request.session['count']
        
    }
    return render(request , 'index2.html',context)