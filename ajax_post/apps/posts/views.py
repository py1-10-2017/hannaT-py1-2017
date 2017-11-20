from django.shortcuts import render, HttpResponse, redirect
from models import Post
from django.core import serializers
import json



def index(request):
    return render(request,'posts/index.html')
def json_posts(request):
    posts = Post.objects.all()
    return HttpResponse(serializers.serialize("json", posts), content_type='application/json')
def post_json(request):
    post = Post.objects.create(post=request.POST.get('post', False))
    return HttpResponse(json.dumps({'post': post.post}), content_type='application/json')

