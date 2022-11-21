from .import views
from django.urls import path
from unicodedata import name

app_name = 'customer_api'
urlpatterns = [
    path('customer_api',views.load_customer,name="customer_api"),
    path('add_customer',views.add_custmer,name="add_customer"),
    path('update_customer/<int:id>',views.update_customer,name="update_customer"),
    path('delete_customer/<int:id>',views.delete_customer,name="delete_customer"),
    path('index',views.index,name="index"),
    path('num',views.num,name="num")                 
]