from django.shortcuts import render

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