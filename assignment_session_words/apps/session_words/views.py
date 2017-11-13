from django.shortcuts import render, HttpResponse, redirect
from django.contrib import sessions
from time import gmtime, strftime

secret_key = "some_secret"

def index(request):
    request.session['words_list'] = request.session.get('words_list', [])
    return render(request,'session_words/index.html')

def process(request):
    size = request.POST.get('size')
    
    new_word = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'time': strftime("%H: %M %p, %b %d, %Y", gmtime()),
        'size': size if size != None else '1em'
    }   
    req = request.session.get('words_list')
    req.append(new_word)
    request.session['words_list'] = req
    return redirect('/')

def clear(request):
    del request.session['words_list']
    return redirect('/')