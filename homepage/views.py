from django.shortcuts import render,redirect
from my_admin.models import myprodect,myvariant,AdminCategory

# Create your views here.
def firstpage(request):
    return render(request,'firstpage.html')

def homepage(request):
    if 'username'in request.session:
        print('homepage here')
        main_category = AdminCategory.objects.all()
        return render(request, 'homepage.html', {'main_category': main_category})
    return render(request,'login.html')

def about(request):
    if 'username'in request.session:
        print('homepage here')
        main_category = AdminCategory.objects.all()
        return render(request, 'homepage.html', {'main_category': main_category})
    return render(request,'login.html')
    


# def edit_category(request):
#     count_pro=myprodect.objects.count()
#     category=AdminCategory.objects.all()
#     return render(request,'edit_category.html',{'category':category})