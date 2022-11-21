from itertools import product
from django.shortcuts import render,redirect
from common.models import Customer, Seller
from customer.decorator import auth_customer
from customer.models import Cart
from seller.models import Product
from django .http import JsonResponse 


# Create your views here.


@ auth_customer                                         #decorator fn
def home(request):
    products = Product.objects.all()
    customer = Customer.objects.get (id = request.session ['userid'])    
    return render(request,'customer/home.html' , {'user_data' : customer,'products':products})   # key for customer id (dictionary)


def product_page(request,p_id):                               #to pass data (id) through url
    product = Product.objects.get(id=p_id)
    return render (request,'customer/product_page.html',{'product':product})    


def Add_to_cart(request,p_id):
    cart = Cart(product_id=p_id,customer_id = request.session['userid'])            #use _id after for foreignkeys
    data_exist = Cart.objects.filter (product_id=p_id,customer_id = request.session['userid']).exists()
    # print (data_exist)
    if data_exist :
        return redirect ('customer:customerhome')    
    cart.save()
    return redirect('customer:customerhome')

@ auth_customer
def cart (request) :
    carts = Cart.objects.all()
    customer = Customer.objects.get(id = request.session ['userid'] )
    return render (request,'customer/cart.html',{'carts':carts ,'customer':customer}) 


def logout (request) :
    del request.session['userid']
    request.session.flush()
    return redirect ('common:common_home')    

def checkout (request,p_id) :
    product = Product.objects.get(id =p_id)
    return render (request,'customer/checkout.html',{"product":product,})    

def remove (request,p_id):
    cart = Cart.objects.get(product_id = p_id ,customer_id= request.session['userid'])
    cart.delete()
    return redirect ('customer:cart')

# def home2(request):
#     products = Product.objects.all()
#     customer = Customer.objects.get (id = request.session ['userid'])   
#     return render(request,'customer/home2.html' , {'user_data' : customer,'products':products}) 

def update_quantity (request) :
    quantity = request.POST ['quantity']
    price = request.POST ['price']
    total = int(quantity) * float (price)
    print (total)
    return JsonResponse ({"total" : total})