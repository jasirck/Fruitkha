from django.urls import path
from account import views


urlpatterns = [
    path('account/',views.account,name='account'),

]