from django.shortcuts import render,redirect
from my_admin.models import myprodect,myvariant,AdminCategory
from login.models import user

# Create your views here.
def firstpage(request):
    if 'username'in request.session:
        log=True
    else:
        log=False
            
    return render(request,'homepage.html',{'log':log})

def homepage(request):
    if 'username'in request.session:
          log=True
    else:
         log=False
    print('homepage here')
    main_category = AdminCategory.objects.all()
    return render(request, 'homepage.html', {'main_category': main_category,'log':log})
    # return render(request,'login.html')
def news(request):
        if 'username'in request.session:
            log=True
        else:
            log=False
    # if 'username'in request.session:
        print('newspage here')
        return render(request, 'news.html',{'log':log} )
    # return render(request,'login.html')

def contact(request):
        if 'username'in request.session:
            log=True
        else:
            log=False
    # if 'username'in request.session:
        print('contactpage here')
        return render(request, 'contact.html',{'log':log} )
    # return render(request,'login.html')

def about(request):
        if 'username'in request.session:
            log=True
        else:
            log=False
    # if 'username'in request.session:
        print('homepage here')
        main_category = AdminCategory.objects.all()
        return render(request, 'homepage.html', {'main_category': main_category,'log':log})
    # return render(request,'login.html')
    


# def edit_category(request):
#     count_pro=myprodect.objects.count()
#     category=AdminCategory.objects.all()
#     return render(request,'edit_category.html',{'category':category})