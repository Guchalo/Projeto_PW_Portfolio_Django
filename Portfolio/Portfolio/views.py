from django.shortcuts import render,redirect

from .models import Post
from .forms import PostForm

def index_view(request):
	return render(request, 'portfolio/index.html')

def projects_view(request):
    return render(request, 'portfolio/projects.html')

def contacts_view(request):
    return render(request, 'portfolio/contacts.html')

def about_view(request):
    return render(request, 'portfolio/about.html')

def playground_view(request):
    return render(request, 'portfolio/playground.html')

def pw_view(request):
    return render(request, 'portfolio/pw.html')

def home_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/home.html', context)

def new_post_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, 'portfolio/new.html', context)


def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')