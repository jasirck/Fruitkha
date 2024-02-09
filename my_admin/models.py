from django.db import models
# from image_cropping import ImageRatioField
# Create your models here.
class AdminCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    category_description = models.TextField()
    offer = models.IntegerField()
    category_image=models.ImageField(upload_to='category_image/',)
    def __str__(self):
        return self.name


class myvariant(models.Model):
    id = models.BigAutoField(primary_key=True)
    variant_name = models.CharField(unique=True, max_length=255)
    def __str__(self):
        return self.variant_name


class myprodect(models.Model):
    id=models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=10, default='list')
    price=models.IntegerField()
    prodect_name=models.CharField(max_length=50,unique=True) 
    category = models.ForeignKey(AdminCategory, on_delete=models.SET_NULL,null=True,related_name='category_products')    
    description=models.TextField()
    quantity=models.IntegerField()
    variant=models.ForeignKey(myvariant, on_delete=models.SET_NULL,null=True, related_name='variant_products')
    offer = models.IntegerField(null=True)
    prodect_image1=models.ImageField(upload_to='image/')
    prodect_image2=models.ImageField(upload_to='image/')
    prodect_image3=models.ImageField(upload_to='image/')
    # cropping = ImageRatioField('image', '225x225')

    def __str__(self):
        return self.prodect_name


class orders(models.Model):
    id=models.BigAutoField(primary_key=True)
    Username=models.CharField(max_length=50)
    price=models.IntegerField()
    phone_number=models.IntegerField()
    prodect_name=models.CharField(max_length=50)
    order_time=models.DateTimeField( auto_now=False, auto_now_add=True) 
    status=models.CharField( max_length=50)

