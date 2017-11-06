from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    context={
        'attempt': 1,
        'random_string': get_random_string(length=14)
    }
    return render(request, 'random_word/index.html', context)


def create(request):

    context = {
        'attempt': int(request.POST['attempt']) + 1,
        'random_string': get_random_string(length=14)
    }   
    return render(request, 'random_word/index.html', context )

def reset(request):
    context={
        'attempt': 1,
        'random_string': get_random_string(length=14)
    }
    return render(request, 'random_word/index.html', context )
    