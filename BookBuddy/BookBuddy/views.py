from django.http import HttpResponse
from django.shortcuts import render
from .PMail import sendmsg
import smtplib, ssl

def home(request):
    c={}
    return render(request,'login.html',c)

def contactus(req):
    return render(req,'contact.html',{})

def sendmail(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    msgtxt=request.POST.get('msg')
    msg="Name  -- "+name+"\nEmail -- "+email+"\nMessage  -- "+msgtxt
    sendmsg(msg)
    return HttpResponse("Thank you for connecting with us")
