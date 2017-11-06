from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "This will be the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "This will display a new form to create blog"
    return HttpResponse(response)
def create(request):
    return redirect('/')
def show(request, blog_id):
    print blog_id
    return HttpResponse("This is display blog{}".format(blog_id))
def edit(request, blog_id):
    return HttpResponse("edit blog{}".format(blog_id))
def delete(request, blog_id):
    return redirect('/')