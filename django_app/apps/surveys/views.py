from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "This will display all the surveys creted"
    return HttpResponse(response)
def new(request):
    response = "This will display form to add new survey"
    return HttpResponse(response)