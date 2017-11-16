from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
import bcrypt
secret_key = "verysecretkey"


def index(request):
    return render(request, 'authentication/index.html')
def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    else:
        password = request.POST['password'].encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User.objects.create(f_name= request.POST['f_name'], l_name= request.POST['l_name'], email = request.POST['email'], password = hashed)
        print user.password
        print hashed
        request.session['id'] = user.id
        request.session['status'] = "registered"
        return redirect('/success')
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    u_password = user.first().password
    
    if user.count() > 0 and user.first().email == email and bcrypt.checkpw(password.encode(), u_password.encode()):
        request.session['id'] = user.first().id
        request.session['status'] = "logged in" 
        return redirect('/success')
    else:
        messages.error(request, "User name and password does not match")
        return redirect('/')

def success(request):
    u = User.objects.filter(id = request.session['id'])
    context={
        'user_f_name': u.first().f_name
        }
    return render(request, 'authentication/success.html', context)