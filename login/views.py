from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from login.models import user
import random
from django.core.mail import send_mail
from django.utils import timezone
from my_admin.models import myprodect,AdminCategory


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            if 'username'in request.session:
                print('homepage here')
                main_category = AdminCategory.objects.all()
                return render(request, 'homepage.html', {'main_category': main_category})
            m = user.objects.get(email=email)
            if m.email== email :
                if (m.password==password):
                    if (m.action=='allow'):
                        request.session['username']=m.username
                        m.status='LOGIN'
                        m.save()
                        return redirect('homepage')
                    else:
                        messages.info(request, 'Sorry Your Blocked !')
                        return redirect('login')
                else:
                    messages.info(request, 'Password Not Match !')
                    return redirect('login.html')
            else:
                messages.info(request, 'Password Not Match !')
                return redirect('login')
        except:
            messages.info(request, 'Username or Password Not Match !')
            return redirect('login')
    return render(request, 'login.html')


otp=0
time=0
fotp=0
ftime=0
user_email='' 
# user_obj=

def otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        email_exists = user.objects.filter(email=email).exists()
        
        if email_exists:
            messages.info(request, 'Email is taken !')
            return redirect('otp')
        else:
            global otp
            global time
            global user_email
            user_email = email
            print(email)
            otp = random.randrange(100000, 999999)
            time =  timezone.now()
            email_from = 'muhammedjck1@gmail.com'
            subject = 'OTP for Login Verification'
            message = 'Your One Time Password: ' + str(otp)
            print(otp)
            send_mail(subject, message, email_from, [email], fail_silently=False)
            return redirect('validation')
    return render(request, 'otp.html')

for_email=''
def forgot_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        email_exists = user.objects.filter(email=email).exists()
        
        if email_exists:
            global fotp
            global for_email
            global ftime
            for_email = email
            fotp = random.randrange(100000, 999999)
            ftime= timezone.now()
            email_from = 'muhammedjck1@gmail.com'
            subject = 'OTP for Login Verification'
            message = 'Your One Time Password: ' + str(fotp)
            print(fotp)
            send_mail(subject, message, email_from, [email], fail_silently=False)
            return redirect('forgot_validation')
        else:
            messages.info(request, 'Email does not exist')
            return redirect('forgot_otp')
    
    return render(request, 'forgot_otp.html')

def forgot_validation(request):
    if request.method == 'POST':
        global fotp
        global ftime
        time_difference = timezone.now() - ftime
        user_otp = request.POST.get('otp')
        print(fotp,'utfydydrykdytdktyd',int(user_otp))
        if fotp == int(user_otp) and time_difference.total_seconds() <= 60 :
            print('success')
            return redirect ('new_password')
        else:
            messages.info(request, 'OTP not match or time out')
            return redirect('forgot_validation')
    return render(request,'forgot_validation.html')


# user_obj=
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number = request.POST.get('number')
        check_num=number
        number=int(number)
        print(check_num)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        global user_email
        print(user_email)
        if password1 == password2 and len(check_num)==10 and check_num[0]!='0':
            if user.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken!')
                print('username take!!!!')
                return redirect('register')
            if username.strip() == '':
                messages.info(request, "Username is emty!")
                print('username emty!!!!')
                return redirect('register')
            else:
                 
                 print(username,'eleseEeEeEeee')
                 user_obj = user(first_name=first_name,email=user_email,last_name=last_name,username=username,number=number,password=password1)
                 print(type(number))
                 user_obj.save()
                 messages.success(request, 'User registered')
                 return redirect('login')  # Redirect to a success page
        else:
            messages.info(request, 'Passwords do not match or number not exixt')
    return render(request,'register.html')

def validation(request):
    if request.method == 'POST':
        global otp
        global time
        time_difference = timezone.now() - time
        user_otp = request.POST.get('otp')
        print(otp,"||",user_otp)
        try :
            if otp == int(user_otp) and time_difference.total_seconds() <= 60 :
                print('success')
                global for_email
                # user_obj.save()
            
                return redirect ('register')
            else:
                messages.info(request, 'OTP not match or time out')
                return redirect('validation')
        except:
            return render(request,'validation.html')
    return render(request,'validation.html')

def new_password(request):
    if request.method == 'POST':
        global for_email
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(otp,'utfydydrykdytdktyd',for_email)
        if password1== password2:
            print('success')
            chenge=user.objects.get(email=for_email)
            print(chenge.password)
            chenge.password=int(password1)
            chenge.save()
            print(password1)
            print(chenge.password)
            return redirect ('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('validation')
    return render(request,'new_password.html')

def logout_user(request):
    if 'username'in request.session:
        username = request.session.get('username', None)
        user_obj = user.objects.get(username=username)
        user_obj.status= 'LOGOUT'
        user_obj.save()
        request.session.flush()
        
        messages.info(request, 'your logout')
        return redirect('login')
    else:
        return redirect('login')
