from .models import User
from django.shortcuts import render
from django.http import HttpResponse


def dele(req):
    User.objects.all().delete()
    return HttpResponse("Users Deleted")