from unicodedata import name
from django.urls import path
from . import views


app_name='common'

urlpatterns=[
    path('customer_signup',views.customer_signup,name="customer_signup"),
    path('',views.home,name="common_home"),
    path('email_exist',views.email_exist,name="email_exist"),
    path('s_email_exist',views.s_email_exist,name='s_email_exist'),
    # path('home2',views.home2,name="home2"),
]