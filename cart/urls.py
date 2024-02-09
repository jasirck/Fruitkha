from django.urls import path
from cart import views


urlpatterns = [
    path('cart_page',views.Cart,name='Cart'),
    path('add_cart<int:id>/',views.add_cart,name='add_cart'),
    path('delete_cart<int:id>',views.delete_cart,name='delete_cart'),
]