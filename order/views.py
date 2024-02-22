from django.shortcuts import render,redirect
from login.models import user,user_address
from my_admin.views import myprodect
from cart.models import cart
from django.db.models import Sum
from order.models import order,order_items
import random
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def checkout(request):
    username = request.session.get('username', None)
    user_obj =user.objects.filter(username=username).prefetch_related('current_address').first()
    address = user_address.objects.filter(user_id=user_obj.id)
    cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
    subtotal= cart.objects.filter(user_id=user_obj.id).aggregate(subtotal=Sum('cart_total'))
    subtotal = subtotal['subtotal'] if subtotal['subtotal'] is not None else subtotal['subtotal']
    if subtotal is None:
        shipping = 0
        subtotal = 0  # Set subtotal to 0 if it's None
    elif subtotal > 1000:
        shipping = 0
    else:
        shipping = 40
    total = subtotal + shipping


    return render(request,'checkout.html',{'user':user_obj,'cart_obj':cart_obj,'subtotal':subtotal,'ship':shipping,'total':total,'address':address})
   

def chenge(request,id):
    if 'username'in request.session:
        user_obj=user.objects.get(id=id)
        address = user_address.objects.filter(user_id=user_obj.id)
        if request.method == 'POST':
            address=request.POST.get('address')
            add=user_address.objects.get(id=address)
            user_id=user.objects.get(id=id)
            user_id.current_address=add
            user_id.save()
            return redirect('checkout')
        return render(request,'chenge.html',{'user':user_obj, 'address':address})
    return render(request,'login.html')


def cod_order(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj =user.objects.filter(username=username).prefetch_related('current_address').first()
        cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
        subtotal= cart.objects.aggregate(subtotal=Sum('cart_total'))
        subtotal = subtotal['subtotal'] if subtotal['subtotal'] is not None else subtotal['subtotal']
        shipping= 0 if subtotal>1000 else 40
        total=subtotal+shipping
        temp='fruitkha'+str(random.randint(111111,999999))
        while order.objects.filter(order_id=temp) is None:
            temp='fruitkha'+str(random.randint(111111,999999))
        ord=order(user=user_obj,total_price=total,payment_method='COD',order_id=temp)
        ord.save()

        for i in cart_obj:
            ord_it=order_items(order_item=ord,product=i.product_id,price_now=i.product_id.price,quantity_now=i.book_quantity)
            temp=myprodect.objects.get(id=i.product_id.id)
            temp.quantity-=i.book_quantity
            temp.save()
            ord_it.save()
        cart_obj.delete()
        return redirect('shop/')
    return render ('shop.html')


def razorpaychek(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj =user.objects.filter(username=username).prefetch_related('current_address').first()
        cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
        subtotal= cart.objects.aggregate(subtotal=Sum('cart_total'))
        subtotal = subtotal['subtotal'] if subtotal['subtotal'] is not None else subtotal['subtotal']
        shipping= 0 if subtotal>1000 else 40
        total=subtotal+shipping
        temp='fruitkha'+str(random.randint(111111,999999))
        while order.objects.filter(order_id=temp) is None:
            temp='fruitkha'+str(random.randint(111111,999999))
        # ord=order(user=user_obj,total_price=total,payment_method='COD',order_id=temp)
        # ord.save()

        # for i in cart_obj:
        #     ord_it=order_items(order_item=ord,product=i.product_id,price_now=i.product_id.price,quantity_now=i.book_quantity)
        #     ord_it.save()
        # cart_obj.delete()
        print('hello razor pay here')
        return JsonResponse({
            'total_price':total,
            'order_id':temp
        })
    return render ('login')


def online_order(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj =user.objects.filter(username=username).prefetch_related('current_address').first()
        cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
        payment_id=request.POST.get('payment_id')
        order_id=request.POST.get('order_id')
        total=request.POST.get('total')
        ord=order(user=user_obj,total_price=total,payment_method='Online',order_id=order_id,payment_id=payment_id)
        ord.save()

        for i in cart_obj:
            ord_it=order_items(order_item=ord,product=i.product_id,price_now=i.product_id.price,quantity_now=i.book_quantity)
            ord_it.save()
            cart_obj.delete()
        return JsonResponse({'status':"Your Order Placed Succesfully"})
    return redirect ('login')


def online_sucess(request):
    return HttpResponse("MyOrder is succesfuly placed")

def edit_address_check(request,id,a_id):
    if 'username'in request.session:
        user_obj=user.objects.get(id=id)
        address=user_address.objects.get(id=a_id)
        if request.method == 'POST':
            address.name=request.POST.get('name')
            address.call_number=request.POST.get('call_number')
            address.house_name=request.POST.get('housename')
            address.lanmark=request.POST.get('lanmark')
            address.post=request.POST.get('post')
            address.city=request.POST.get('city')
            address.state=request.POST.get('state')
            address.pincode=request.POST.get('pincode')
            address.user_id=user.objects.get(id=id)
            print('before')
            # address=user_address(user_id=user_id,name=name,call_number=call_number,house_name=house_name,lanmark=lanmark,post=post,city=city,state=state,pincode=pincode)
            print('after')
            print(address.user_id,address.name,address.call_number,type(address.call_number),address.house_name,address.lanmark,address.post,address.city,address.pincode,address.state)
            address.save()
            return redirect('account')
        return render(request,'account_edit_address.html',{'user':user_obj,'address':address})
    return render(request,'login.html')