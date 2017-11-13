from django.shortcuts import render, redirect, HttpResponse

def index(request):
    request = 'Hello'
    return HttpResponse(request)