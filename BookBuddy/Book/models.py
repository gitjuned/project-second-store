from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    useremail=models.EmailField(primary_key=True,unique=True)
    userpassword=models.CharField(max_length=50)
    userphone=models.CharField(max_length=50,unique=True)
    useraddress=models.CharField(max_length=200)
    userstream=models.CharField(max_length=50)