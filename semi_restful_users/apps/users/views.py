from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {'users': User.objects.all()})
def new(request):
    return render(request, 'users/new.html')
def show(request, id):
    return render(request, 'users/show.html', {'user': User.objects.get(id = id)})
def edit(request, id):
    return render(request, 'users/edit.html', {'user': User.objects.get(id = id)})
def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/blog/edit/'+id)
    else:
        user = User.objects.get(id = id)
        user.f_name = request.POST['f_name']
        user.l_name = request.POST['l_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users')
def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users')
    else:
        User.objects.create(f_name= request.POST['f_name'], l_name= request.POST['l_name'], email = request.POST['email'])
        return redirect('/users')
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')
