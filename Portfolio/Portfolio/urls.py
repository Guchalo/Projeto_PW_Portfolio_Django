"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('index/', views.index_view,name='index'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('playground/', views.playground_view, name='playground'),
    path('projects/', views.projects_view, name='projects'),
    path('pw/', views.pw_view, name='pw'),
    path('home/', views.home_view,name='home'),
    path('new/', views.new_post_view, name='new'),
    path('edita/<int:post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_post_view, name='apaga'),
    
    
]
