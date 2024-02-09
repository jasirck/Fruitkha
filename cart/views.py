from django.shortcuts import render,redirect
from my_admin.models import myprodect
from login.models import user
from cart.models import cart
from django.contrib import messages




# Create your views here.
def Cart(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj = user.objects.get(username=username)
        cart_obj = cart.objects.filter(user_id=user_obj.id).prefetch_related("product_id")
        
        return render(request,'cart.html',{'cart_obj':cart_obj})
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
                    cart_obj =cart(user_id=user_id,product_id=product_id,book_quantity=int(quantity))
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
    
