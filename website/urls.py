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
from website.views import *
from django.contrib.sitemaps.views import sitemap
from  website.sitemaps import WebsiteStaticSitemap
from blog.sitemaps import BlogSitemap
from django.urls import include
from django.urls import re_path
from django.views.generic import TemplateView


app_name = 'website'
sitemaps = {
    'static': WebsiteStaticSitemap,
    'blog':BlogSitemap
    
}

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('news_letter/',news_letter,name='news_letter'),
    path(
    "sitemap.xml",sitemap,{"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt',include('robots.urls')),
    

]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

# urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='commingsoon.html'), name='maintenance'))

