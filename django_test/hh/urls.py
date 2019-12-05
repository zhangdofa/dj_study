"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# from stock import views
# from django.urls import path
from django.views.generic.base import TemplateView

from .views import index
urlpatterns = [
    url('home', TemplateView.as_view(template_name=r'F:\python project\dj_study\django_test\hh\templates\tb\index.html'), name='echarts-url'),

    url('data/index.json', index, name='api-echarts')
]
