from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from my_admin.models import myprodect,myvariant,AdminCategory

# Create your views here.
# @login_required(login_url="/accounts/login/")
def shop(request):
    # if 'username'in request.session:
        if 'username'in request.session:
            log=True
        else:
            log=False
        main_prodect=myprodect.objects.filter(category__status='list',quantity__gt=0).order_by('prodect_name')
        main_category = AdminCategory.objects.filter(status="list").order_by('name')
        return render(request,'shop.html',{'main_prodect':main_prodect,'main_category': main_category,'log':log})
    # return render(request,'login.html')
    

def shop_cat(request, id):
    if 'username'in request.session:
        log=True
    else:
        log=False
    prodects =myprodect.objects.filter(category=id,quantity__gt=0,category__status='list')
    main_category = AdminCategory.objects.filter(status="list").order_by('name')
    hover=id
    return render(request, 'shop.html', {'main_prodect': prodects, 'main_category': main_category,'hover':hover,'log':log})
    
def single_prodect(request,id):
    if 'username'in request.session:
        if 'username'in request.session:
            log=True
        else:
            log=False
        left=False
        single=myprodect.objects.get(id=id)
        if single.quantity <= 11:
            left=True
            # single.quantity=5
            # single.save()
        cate=single.category
        var=single.variant
        return render(request,'single_product.html',{'single_product':single,'cate':cate,'var':var,'log':log,'left':left})
    return render(request,'login.html')
  

def single_prodect_img(request,id,img):
    if 'username'in request.session:
        single=myprodect.objects.get(id=id)
        cate=single.category
        var=single.variant
        return render(request,'single_product.html',{'single_product':single,'cate':cate,'var':var,'img':img})
    return render(request,'login.html')
    