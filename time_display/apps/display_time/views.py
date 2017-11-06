from django.shortcuts import render, HttpResponse, redirect 
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    print "Hello"
    print context
    return render(request,'display_time/index.html', context)





