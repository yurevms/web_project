from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseNotFound
from django.urls import reverse
from .models import Post
from .form import CommentsForm

def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})

def create(request):
    if request.method == 'POST':
        post = Post()
        post.name = request.POST.get('name')
        post.text_data = request.POST.get('text_data')
        post.photo = request.FILES.get('photo')
        post.save()
        return HttpResponseRedirect(reverse('website:index'))
    return render(request, 'create.html')

def delete(request, id):
    try:
        post = Post.objects.get(id = id)
        post.delete()
        return HttpResponseRedirect('/website/')
    except:
        return HttpResponseNotFound('<h2> Post not found </h2>')

def details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'details.html', {'post': post})

def comm(request, id):
    form = CommentsForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.post_id = id
        form.save()
    return redirect(f'/{id}')


def rules(request):
    return render(request, "rules.html", {'rules': rules})

def info(request):
    return render(request, "info.html", {'info': info})