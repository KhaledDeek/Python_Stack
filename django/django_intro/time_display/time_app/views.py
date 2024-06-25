from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M %p")
    }
    return render(request,'index.html', context)

