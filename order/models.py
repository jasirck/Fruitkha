from django.db import models
from login.models import user,user_address
from my_admin.models import myprodect
from django.utils import timezone
# Create your models here.

class order(models.Model):
    id=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE,null=False)
    total_price=models.FloatField(null=False)
    payment_method=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    status=models.CharField(max_length=150,null=False,default='Pending')
    msg=models.TextField(null=True)
    order_id=models.CharField(max_length=150,null=True)
    created=models.DateField(auto_now_add=True)
    expect = models.DateField(default=timezone.now() + timezone.timedelta(days=6))
    updated=models.DateField(auto_now=True)

class order_items(models.Model):
    order_item=models.ForeignKey(order, on_delete=models.CASCADE)
    product=models.ForeignKey(myprodect, on_delete=models.CASCADE)
    price_now=models.FloatField()
    quantity_now=models.IntegerField()
