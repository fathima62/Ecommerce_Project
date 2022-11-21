from itertools import product
from unicodedata import name
from django.urls import path
from . import views


app_name='customer'

urlpatterns=[
    path('home',views.home,name="customerhome"),
    path('product/<int:p_id>',views.product_page,name="product_page"),                    #to get product id through url
    path('add_to_cart/<int:p_id>',views.Add_to_cart,name="add_to_cart"),
    path('cart',views.cart,name='cart'),
    path('logout',views.logout,name="logout"),
    path('checkout/<int:p_id>',views.checkout,name="checkout"),
    path('remove/<int:p_id>',views.remove,name="remove"),
    path('update_quantity',views.update_quantity,name="update_quantity")
    #  path('home2',views.home2,name="customerhome2"),
]