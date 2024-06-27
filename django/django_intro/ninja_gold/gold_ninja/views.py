from django.shortcuts import render , redirect
import random 	          
from time import strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if 'rand' not in request.session:
        request.session['rand'] = 0
    request.session['gold'] += request.session['rand']
    
    if 'msg' not in request.session:
        request.session['msg'] = []  
    
    if 'count' not in request.session:
        request.session['count'] = 0
    
    context = {
        "gold" : request.session['gold'],
        "msg" : ''.join(request.session['msg'])
    }

    return render(request , 'index.html' , context)

def gold(request):
    request.session['count'] +=1
    request.session['rand'] = random.randint(int(request.POST['rangex']) , int(request.POST['rangey']))
    request.session['building'] = request.POST['building']
    
    if int(request.session['rand']) > 0 :
        request.session['msg'].insert(0 , f"<li class='earned'><h6>You entered a {request.session['building']} and earned {request.session['rand']} golds ({strftime("%B %d %Y %I:%M %p")})</h6></li>")
    
    if int(request.session['rand']) < 0 :
        request.session['msg'].insert(0 , f"<li class='lost'><h6>You failed a quest and lost {request.session['rand']} . Ouch.. ({strftime("%B %d %Y %I:%M %p")})</h6></li>")
    
    
    if int(request.session['count']) > 15 and int(request.session['gold']) < 500:
        request.session['msg'].clear()
        request.session['msg'].append('<h1>You Lose</h1>')
    
    if int(request.session['count']) < 15 and int(request.session['gold']) > 500:
        request.session['msg'].clear()
        request.session['msg'].append('<h1>You Win</h1>')


    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['rand']
    del request.session['msg']
    del request.session['count']
    return redirect('/')