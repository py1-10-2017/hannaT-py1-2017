from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "hi"
    return HttpResponse(response)