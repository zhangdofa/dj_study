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
from django.contrib import admin

# from django_test import hh
from .views import home, person, login, register, index, logout, test, play, logout1, login1, register1, upimg, upvideo, \
    uppassword, upphone, delete, index1, index2, find, review, refuse, administrator, b_pass, b_refuse, c_refuse, \
    logout2, play1, delete1, ll

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'h/',home),
    url(r'test/',test),
    url(r'home/',index),
    url(r'home1/',index1),
    url(r'home2/',index2),
    url(r'person/',person),
    url(r'login/',login),
    url(r'login1/',login1),
    url(r'logout/',logout),
    url(r'logout1/',logout1),
    url(r'logout2/',logout2),
    url(r'register/',register),
    url(r'register1/',register1),
    url(r'playpage/',play),
    url(r'playpage1/',play1),
    url(r'upimg',upimg),
    url(r'upvideo',upvideo),
    url(r'uppassword',uppassword),
    url(r'upphone',upphone),
    url(r'delete',delete),
    url(r'cacel',delete1),
    url(r'll',ll),
    url(r'find',find),
    url(r'review',review),
    url(r'refuse',refuse),
    url(r'administrator',administrator),
    url(r'pass',b_pass),
    url(r'reject',b_refuse),
    url(r'town_down',c_refuse)
]
