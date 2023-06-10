from django.shortcuts import render

def index_view(request):
	return render(request, 'Portfolio/index.html')

def projects_view(request):
    return render(request, 'Portfolio/projects.html')

def contacts_view(request):
    return render(request, 'Portfolio/contacts.html')

def about_view(request):
    return render(request, 'Portfolio/about.html')

def playground_view(request):
    return render(request, 'Portfolio/playground.html')

def pw_view(request):
    return render(request, 'Portfolio/pw.html')