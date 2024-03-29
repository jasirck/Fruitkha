from django.urls import path
from account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account',views.Account,name='account'),
    path('add_address<int:id>',views.add_address,name='add_address'),
    path('edit_address<int:id>/<int:a_id>',views.edit_address,name='edit_address'),
    path('delete_address<int:id>/<int:a_id>',views.delete_address,name='delete_address'),
    path('add_address<int:id>',views.add_address,name='add_address'),
    path('current_address<int:id>',views.current_address,name='current_address'),
    path('edit_user<int:id>',views.edit_user,name='edit_user'),
    path('chenge_password',views.chenge_password,name='chenge_password'),
    path('chenge_email',views.chenge_email,name='chenge_email'),
    path('chenge_email_validation',views.chenge_email_validation,name='chenge_email_validation'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)