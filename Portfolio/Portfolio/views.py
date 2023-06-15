from django.shortcuts import get_object_or_404, render,redirect

from .models import Post
from .forms import PostForm
import requests
from bs4 import BeautifulSoup

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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'portfolio/new.html', {'form': form})


def edita_post_view(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = PostForm(instance=post)

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('home')

def LEI_view(request):

    lista_cadeiras = []

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

    

    url = 'https://github.com/Guchalo/Projeto_PW_Portfolio_Django'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    div = soup.find('div',class_='plain')

    pre = div.find('pre').text

    

    return render(request, 'portfolio/LEI.html',{
            'lista': pre,
            
    })