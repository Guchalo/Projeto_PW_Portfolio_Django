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
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('index/', views.index_view,name='index'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('projects/', views.projects_view, name='projects'),
    path('home/', views.home_view,name='home'),
    path('new/', views.new_post_view, name='new'),
    path('LEI/', views.LEI_view, name='LEI'),
    path('edita/<int:post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_post_view, name='apaga'),   
]
urlpatterns += static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT)
