from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from my_admin.models import myprodect,AdminCategory,myvariant
from login.models import user
from my_admin.forms import prodectsForm
from order.models import order



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,'utfydydrykdytdktyd')
        if request.user.is_authenticated:
            
            print('I think your is login')
            return redirect('dashboard')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("User authenticated:", user)
            return redirect('dashboard')
        else:
            # Authentication failed
            print("Authentication failed")
            messages.success(request, 'Username or Password is Wrong !')
            return redirect('admin_login')
    return render(request,'login_admin.html')

@login_required(login_url='admin_login')
def dashbord(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        order_count=order.objects.count()
        return render(request,'dashboard.html',{'users':count,'pro':count_pro,'ord':order_count})
    return render(request,'404.html')
    

@login_required(login_url='admin_login')
def management(request):
    if 'username'not in request.session:
        users=user.objects.all().order_by('id')
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        order_count=order.objects.count()
        return render(request,'management.html',{'user':users,'users':count,'pro':count_pro,'ord':order_count})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def add_prodect(request):
    if 'username'not in request.session:
        print("add prodect here")
        option=AdminCategory.objects.all()
        variant_option=myvariant.objects.all()
        count = user.objects.count()
        count_pro=myprodect.objects.count()
        form = prodectsForm(request.POST, request.FILES)
    
    
        if request.method == 'POST':
            prodect_name = request.POST.get('prodect_name')
            category = request.POST.get('category')
            variant = request.POST.get('variant')
            price = request.POST.get('price') 
            description = request.POST.get('description')
            quantity = request.POST.get('quantity')  
            print(variant)
            prodect_image1 = request.FILES.get('image1', None)
            prodect_image2 = request.FILES.get('image2', None) 
            prodect_image3 = request.FILES.get('image3', None)
            variant_id=myvariant.objects.get(id=variant)
            category_id=AdminCategory.objects.get(id=category)
            print(variant_id)
            print(category_id)
        # add=prodects(prodect_name=prodect_name)
            try:
                add = myprodect(prodect_name =prodect_name ,price=price,description=description,quantity=quantity,category=category_id,variant=variant_id, prodect_image1=prodect_image1,prodect_image2=prodect_image2,prodect_image3=prodect_image3)
                add.save()  
                messages.success(request, 'added prodect')
                return redirect('add_prodect') 
            except:
                messages.success(request, 'prodect takin awey')
                return redirect('add_prodect') 
        return render(request, 'add_prodect.html', {'users': count, 'form': form,'categories': option , 'variants': variant_option,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def edit_prodect(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        prodect=myprodect.objects.filter(status='list')
        return render(request,'edit_prodect.html',{'values':prodect,'users':count,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def category(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        order_count=order.objects.count()
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            offer = request.POST.get('offer')
            category_description = request.POST.get('category_description')
            category_image = request.FILES.get('category_image', None)
            print(category_name)
            print(category_name ,'eleseEeEeEeee')
            category_obj = AdminCategory(name =category_name,offer=offer,category_description=category_description,category_image=category_image)
            category_obj.save()
            messages.success(request, 'category aded')
            return redirect('category')  # Redirect to a success page
        return render(request,'category.html',{'users':count,'pro':count_pro,'ord':order_count})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def edit_category(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        category=AdminCategory.objects.filter(status='list')
        order_count=order.objects.count()
        return render(request,'edit_category.html',{'category':category,'users':count,'pro':count_pro,'ord':order_count})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def delete_category(request,id):
    if 'username'not in request.session:
        delete_ca=AdminCategory.objects.get(id=id)
        delete_ca.status='unlist'
        delete_ca.save()
        messages.success(request, 'delete category')
        return redirect('edit_category')
    return render(request,'404.html')

@login_required(login_url='admin_login')
def edit_category_page(request,id):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        category=AdminCategory.objects.get(id=id)
        if request.method == 'POST':
            category.name = request.POST['category_name']
            category.offer = request.POST['offer']
            category.category_description = request.POST['category_description']
            if 'image1' in request.FILES:
                category.category_image = request.FILES['image1']
            category.save()
            messages.success(request, 'edit category')
            return redirect('edit_category') 
        return render(request,'edit_category_page.html',{'category':category,'users':count,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def category_deleted(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        unlist=AdminCategory.objects.filter(status='unlist')
        return render(request,'category_deleted.html',{'unlist':unlist,'users':count,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def readd_category(request,id):    
    if 'username'not in request.session:
        deleted=AdminCategory.objects.get(id=id)
        deleted.status='list'
        deleted.save()
        return redirect('category_deleted')
    return render(request,'404.html')

@login_required(login_url='admin_login')
def variant(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        if request.method == 'POST':
            name = request.POST.get('variant_name')
            print(name)
            print(name ,'eleseEeEeEeee')
            variant_obj = myvariant(variant_name =name)
            variant_obj.save()
            messages.success(request, 'variant aded')
            return redirect('variant')  
        return render(request,'variant.html',{'users':count})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def edit_variant(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        variant=myvariant.objects.all()
        return render(request,'edit_variant.html',{'variant':variant,'users':count,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def delete_variant(request,id):
    if 'username'not in request.session:
        de=myvariant.objects.get(id=id)
        de.status='unlist'
        de.save()
        messages.success(request, 'variant aded')
        return redirect ('edit_variant')
    return render(request,'404.html')

@login_required(login_url='admin_login')
def edit_prodect_page(request,id):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        option=AdminCategory.objects.all()
        variant_option=myvariant.objects.all()
        prodect=myprodect.objects.get(id=id)
        if request.method == 'POST':
            prodect.prodect_name = request.POST['prodect_name']
            category = request.POST.get('category')
            variant = request.POST.get('variant')
            variant_id=myvariant.objects.get(id=variant)
            category_id=AdminCategory.objects.get(id=category)
            prodect.category = category_id
            prodect.price = request.POST['price']
            prodect.description = request.POST['description']
            quantity = float(request.POST['quantity'])
            prodect.quantity=int(quantity)
            prodect.variant = variant_id

            if 'image1' in request.FILES:
                prodect.prodect_image1 = request.FILES['image1']
            if 'image2' in request.FILES:
                prodect.prodect_image2 = request.FILES['image2']
            if 'image3' in request.FILES:
                prodect.prodect_image3 = request.FILES['image3']

            prodect.save()
            messages.success(request, 'edit prodect')
            return redirect('add_prodect') 
        return render(request,'edit_prodect_page.html',{'prodect':prodect,'users':count,'pro':count_pro,'categories': option , 'variants': variant_option})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def action (request,id):
    if 'username'not in request.session:
        act=user.objects.get(id=id)
        if act.action=='allow':
            act.action='block'
            act.save()
            return redirect('management')
        if act.action=='block':
            act.action='allow'
            act.save()
            return redirect('management')
    return render(request,'404.html')


@login_required(login_url='admin_login')
def unlist(request,id):
    deleted=myprodect.objects.get(id=id)
    deleted.status='unlist'
    deleted.save()
    return redirect('edit_prodect')

@login_required(login_url='admin_login')
def deleted(request):
    if 'username'not in request.session:
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        unlist=myprodect.objects.filter(status='unlist')
        return render(request,'deleted.html',{'unlist':unlist,'users':count,'pro':count_pro})
    return render(request,'404.html')

@login_required(login_url='admin_login')
def delete(request,id):    
    deleted=myprodect.objects.objects.get(id=id)
    deleted.delete()
    return redirect('deleted')

@login_required(login_url='admin_login')
def readd(request,id):    
    deleted=myprodect.objects.get(id=id)
    deleted.status='list'
    deleted.save()
    return redirect('deleted')

@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    print('user logout')
    messages.info(request, 'your logout')
    return render(request,'login_admin.html')

@login_required(login_url='admin_login')
def orders(request):    
    if 'username'not in request.session:
        ord=order.objects.all()
        count=user.objects.count()
        count_pro=myprodect.objects.count()
        order_count=order.objects.count()
        return render(request,'orders.html',{'order':ord,'users':count,'pro':count_pro,'ord':order_count})
    return render(request,'404.html')