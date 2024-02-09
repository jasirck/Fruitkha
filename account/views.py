from django.shortcuts import render,redirect
from login.models import user,user_address
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.utils import timezone

# Create your views here.
def Account(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj =user.objects.filter(username=username).prefetch_related('current_address').first()
        address = user_address.objects.filter(user_id=user_obj.id)
        n=0
        return render(request,'account.html',{'user': user_obj, 'address':address,})
    return render(request,'login.html')

def add_address(request,id):
    user_obj=user.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        call_number=request.POST.get('call_number')
        house_name=request.POST.get('housename')
        lanmark=request.POST.get('lanmark')
        post=request.POST.get('post')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        user_id=user.objects.get(id=id)
        print('before')
        address=user_address(user_id=user_id,name=name,call_number=call_number,house_name=house_name,lanmark=lanmark,post=post,city=city,state=state,pincode=pincode)
        print('after')
        print(address.user_id,address.name,address.call_number,type(address.call_number),address.house_name,address.lanmark,address.post,address.city,address.pincode,address.state)
        address.save()
        return redirect('add_address',id)
    return render(request,'account_add_address.html',{'user':user_obj})
    

def current_address(request,id):
    user_obj=user.objects.get(id=id)
    address = user_address.objects.filter(user_id=user_obj.id)
    if request.method == 'POST':
        address=request.POST.get('address')
        add=user_address.objects.get(id=address)
        user_id=user.objects.get(id=id)
        user_id.current_address=add
        user_id.save()
        return redirect('account')
    return render(request,'current_address.html',{'user':user_obj, 'address':address})

def edit_user(request,id):
    user_obj=user.objects.get(id=id)
    if request.method == 'POST':
        print('inside')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number = request.POST.get('number')
        if 'image' in request.FILES:
            image = request.FILES['image']
            user_obj.user_dp=image
        if 10 != len(number) or number[1] =='0':
            print('failed')
            return redirect("account")
        user_obj.username=username
        user_obj.first_name=first_name
        user_obj.last_name=last_name
        user_obj.number
        user_obj.save()
        return redirect("account")
    print('outside')
    return redirect("account")

def chenge_password(request):
    username = request.session.get('username', None)
    user_obj=user.objects.get(username=username)
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if user_obj.password == old_password:
            if new_password == confirm_password:
                user_obj.password=new_password
                user_obj.save()
                messages.success(request, 'Password is chenged')
                return redirect("account")
            else:
                messages.success(request, 'Password somthing else')
                return redirect("chenge_password")
        else:
            messages.success(request, 'Old Password is Wrong')
            return redirect('chenge_password')
    return render(request , 'chenge_password.html',{'user':user_obj})

otp=0
time=0
user_email='' 

def chenge_email(request):
    username = request.session.get('username', None)
    user_obj=user.objects.get(username=username)
    if request.method == 'POST':
        email = request.POST.get('email')
        email_exists = user.objects.filter(email=email).exists()
        if email_exists:
            messages.info(request, 'Email is taken !')
            return redirect('chenge_email')
        else:
            global otp
            global time
            global user_email
            user_email = email
            print(email)
            otp = random.randrange(100000, 999999)
            time =  timezone.now()
            print(time)
            email_from = 'muhammedjck1@gmail.com'
            subject = 'OTP for Login Verification'
            message = 'Your One Time Password: ' + str(otp)
            print(otp)
            send_mail(subject, message, email_from, [email], fail_silently=False)
            return redirect('chenge_email_validation')        
    return render(request,'chenge_email.html',{'user':user_obj})

def chenge_email_validation(request):
    username = request.session.get('username', None)
    user_obj=user.objects.get(username=username)
    if request.method == 'POST':
        global otp
        global time
        now=timezone.now()
        print(timezone.now(),time,'|||',type(timezone.now()),type(time),type(now))
        time_difference = timezone.now() - time
        user_otp = request.POST.get('OTP')
        print(otp,type(otp),"||",user_otp,type(user_otp))
        if int(time_difference.total_seconds()) <= 60 :
            if  otp == int(user_otp):
                print('success')
                global user_email
                print(user_email)
                user_obj.email=user_email
                user_obj.save()
                messages.info(request, 'Email chenged')
                return redirect ('account')
            else:
                messages.info(request, 'OTP not match ')
                return redirect('chenge_email_validation')
        else:
            messages.info(request, 'time out')
            return redirect('chenge_email')
    return render(request,'chenge_email_validation.html',{'user':user_obj})
