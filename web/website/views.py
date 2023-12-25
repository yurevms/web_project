from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from .models import Post

def index(request):
    post = Post.objects.all()
    return render(request, 'website/index.html', {'posts': post})

def create(request):
    if request.method == 'POST':
        post = Post()
        post.name = request.POST.get('name')
        post.text_data = request.POST.get('text_data')
        post.photo = request.FILES.get('photo')
        post.save()
        return HttpResponseRedirect(reverse('website:index'))
    return render(request, 'website/create.html')

def delete(request, id):
    try:
        post = Post.objects.get(id = id)
        post.delete()
        return HttpResponseRedirect('/website/')
    except:
        return HttpResponseNotFound('<h2> Post not found </h2>')


# лайки
def like_post(request, id):
    post = Post.objects.get(id = id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect('/website/')