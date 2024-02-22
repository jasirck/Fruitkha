from django.urls import path
from order import views


urlpatterns = [
    path('checkout',views.checkout,name='checkout'),
    path('chenge<int:id>',views.chenge,name='chenge'),
    path('cod_order',views.cod_order,name='cod_order'),
    path('proceed_to_pay',views.razorpaychek),
    path('online_order/',views.online_order,name='online_order'),
    path('online_sucess/',views.online_sucess,name="online_sucess"),
    path('edit_address_check<int:id>/<int:a_id>',views.edit_address_check,name='edit_address_check'),
    
]