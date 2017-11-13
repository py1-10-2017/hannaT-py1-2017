from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages, sessions
secret_key = 'somesecret'

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method == 'POST':
        counter = request.session.get('counter', 0)
        request.session['counter'] = counter + 1
        new_user = {
            'name': request.POST['name'],
            'loc': request.POST['loc'],
            'language': request.POST['language'],
            'comment': request.POST['comment']
        }
        
        users_list = request.session.get('users',[])
        users_list.append(new_user)
        request.session['users'] = users_list
    return redirect('/surveys/result')

def result(request):
    users = request.session.get('users')
    user = users[len(users) - 1]
    counter = request.session.get('counter', 0)
    return render(request, 'surveys/result.html', {'user': user, 'counter': counter})
