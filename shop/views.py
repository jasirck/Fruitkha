from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from my_admin.models import myprodect,myvariant,AdminCategory

# Create your views here.
# @login_required(login_url="/accounts/login/")
def shop(request):
    if 'username'in request.session:
        main_prodect=myprodect.objects.all().order_by('prodect_name')
        main_category = AdminCategory.objects.all().order_by('name')
        return render(request,'shop.html',{'main_prodect':main_prodect,'main_category': main_category})
    return render(request,'login.html')
    

def shop_cat(request, id):
    if 'username'in request.session:
        prodects =myprodect.objects.filter(category=id)
        main_category = AdminCategory.objects.all().order_by('name')
        hover=id
        return render(request, 'shop.html', {'main_prodect': prodects, 'main_category': main_category,'hover':hover})
    return render(request,'login.html')
    
def single_prodect(request,id):
    if 'username'in request.session:
        single=myprodect.objects.get(id=id)
        cate=single.category
        var=single.variant
        return render(request,'single_product.html',{'single_product':single,'cate':cate,'var':var})
    return render(request,'login.html')
  

def single_prodect_img(request,id,img):
    if 'username'in request.session:
        single=myprodect.objects.get(id=id)
        cate=single.category
        var=single.variant
        return render(request,'single_product.html',{'single_product':single,'cate':cate,'var':var,'img':img})
    return render(request,'login.html')
    