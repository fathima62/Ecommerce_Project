from unicodedata import name
from django.urls import path
from . import views

app_name='seller'
urlpatterns=[
    path('home',views.home,name="home"),
    path('catalogue',views.catalogue,name="catalogue"),
    path('orders',views.orders,name="orders"),
    path('change password',views.change_password,name="change_password"),
    path('add product',views.add_product,name="add_product"),
    path('stock update',views.stock_update,name="stock update")
]