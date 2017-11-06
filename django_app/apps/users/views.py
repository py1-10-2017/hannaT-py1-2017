from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "This will display all the users creted"
    return HttpResponse(response)
def new(request):
    response = "This will display forms for users to create"
    return HttpResponse(response)
def create(request):
    response = "This will create a new user record"
    return HttpResponse(response)


