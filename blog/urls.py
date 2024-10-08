"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from blog.views import *


app_name = 'blog'
urlpatterns = [
    path('',blog_view,name='index'),
    path('blog_single/<int:post_id>',blog_single,name='blog_single'),
    path('category/<str:cat_name>',blog_view,name='blog_cate'),
    path('author/<str:author_username>',blog_view,name='blog_author'),
    path('search/',blog_search,name='blog_search'),
    
    path('test/<str:name>',test)
]
