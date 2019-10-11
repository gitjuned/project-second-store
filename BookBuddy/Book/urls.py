from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from . import views
from . import deleteall

urlpatterns = [
  #  path('home/',views.home),
   # path('',views.home),

    url('addbookdb',views.addBookdb),
    url(r'^book/(?P<pk>\d+)$', views.usertestBook),
    url('login',views.login),
    url('verify',views.verify),
    url('signup',views.register),
    #url('deleteall/',deleteall.dele),
    url('useradd',views.adduser),
    url('forgot',views.forgotpass),
    url('reset',views.resetpass),
    url('addbook',views.addBook),
    url('viewbook',views.viewbook),
    url('logout',views.userlogout),
    url('testbook',views.usertestBook),
    url('dashboard',views.dashboard),
    url(r'^search/([^/]*)',views.search),
    url(r'^getcat/([^/]*)',views.cat),
    url('',views.viewbook),
]