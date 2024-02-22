from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=350, unique=True)
    number = models.BigIntegerField()
    password = models.CharField(max_length=10)
    user_dp=models.ImageField(upload_to='media/user_dp/',default='media/user_dp/user.jpg')
    current_address=models.ForeignKey("user_address", related_name=("address"),null=True ,on_delete=models.SET_NULL)
    action = models.CharField(max_length=10, default='allow')
    status = models.CharField(max_length=10, default='active')
    last_join = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)

class user_address(models.Model):
    id = models.AutoField(primary_key=True)
    user_id=models.ForeignKey(user, on_delete=models.CASCADE, related_name='user_address')
    name=models.CharField( max_length=50)
    call_number=models.BigIntegerField()
    house_name=models.CharField( max_length=100)
    lanmark=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()

    
                              