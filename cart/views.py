from django.shortcuts import render,redirect
from my_admin.models import myprodect
from login.models import user
from cart.models import cart
from django.contrib import messages
from django.db.models import Sum,Q
from django.http import JsonResponse




# Create your views here.
def Cart(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj = user.objects.get(username=username)
        cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
        subtotal_query = cart.objects.filter(Q(user_id=user_obj.id)).aggregate(subtotal=Sum('cart_total'))
        subtotal = subtotal_query['subtotal'] if subtotal_query['subtotal'] is not None else 0

        shipping= 0 if int(subtotal) >1000 else 0 if int(subtotal) == 0 else 40
        total=subtotal+shipping
        return render(request,'cart.html',{'cart_obj':cart_obj,'subtotal':subtotal,'ship':shipping,'total':total
        })
    return render(request,'login.html')

def add_cart(request,id):
    if 'username'in request.session:
        print('add  cart   here  **88888**888*88*88')
        if request.method == 'POST':
            username = request.session.get('username',None)
            user_id = user.objects.get(username=username)
            quantity=request.POST.get('quantity')
            product_id =  myprodect.objects.get(id=id)
            print('dddd',user_id.id,'aaaaa',quantity,"quantity")
            if quantity.strip() is not None:
                try:
                    if product_id.quantity < int(quantity):
                        messages.success(request, "We did't have that much quantity")
                        return redirect("single_prodect",id)
                    cart_obj =cart(user_id=user_id,product_id=product_id,book_quantity=int(quantity),cart_total=int(quantity)*product_id.price)
                    cart_obj.save()
                    messages.success(request, 'added to cart')
                    return redirect("single_prodect",id)#,'success.html'
                except ValueError:
                    messages.success(request, 'can not add without quantity')
                    return redirect("single_prodect",id)# {'message': 'Invalid quantity'}
            else:
                messages.success(request, 'can not add without quantity')
                return redirect("single_prodect",id)#, {'message': 'Quantity cannot be empty'}            
        return redirect("single_prodect",id)
    return render(request,'login.html')

def delete_cart(request,id):
    delete=cart.objects.get(id=id)
    delete.delete()
    return redirect('Cart')

# def plus_cart(request,id,price):
#     plus=cart.objects.get(id=id)
#     print(plus.product_id)
#     plus.book_quantity+=1
#     if plus.product_id.quantity < int(plus.book_quantity or  int(plus.book_quantity ) < 10 ):
#         messages.success(request, "We did't have that much quantity")
#         return redirect('Cart')
#     plus.cart_total=price * plus.book_quantity
#     plus.save()
#     messages.success(request, "quantity ingrees")
#     return redirect('Cart')
    
# def minus_cart(request,id,price):
#     plus=cart.objects.get(id=id)
#     print(plus.product_id)
#     plus.book_quantity-=1

#     plus.cart_total=price * plus.book_quantity
#     plus.save()
#     return redirect('Cart')



def plus_cart(request, id, price):
    cart_item = Cart.objects.get(id=id)
    cart_item.book_quantity += 1
    cart_item.cart_total = price * cart_item.book_quantity
    cart_item.save()
    return JsonResponse({'book_quantity': cart_item.book_quantity})

def minus_cart(request, id, price):
    plus = cart.objects.get(id=id)
    print(plus.product_id)
    plus.book_quantity -= 1
    plus.cart_total = price * plus.book_quantity
    plus.save()
    return JsonResponse({'book_quantity': plus.book_quantity})
