from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=350, unique=True)
    number = models.IntegerField()
    password = models.CharField(max_length=10)
    address = models.TextField()  
    action = models.CharField(max_length=10, default='active')
    status = models.CharField(max_length=10, default='active')
    last_join = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)



