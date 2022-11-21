from itertools import product
from urllib import request
from django.shortcuts import render,redirect

from common.models import Seller
from seller.models import Product

# Create your views here.
def home (request):
    seller = Seller.objects.get (id = request.session ['sellerid'])
    products = Product.objects.all()       
    return render(request,'seller/home.html' , {'user_data' : seller ,"product":products})

def orders (request):
    return render(request,'seller/orders.html')    

def change_password (request):
    msg = ''
    if request.method == 'POST' :
        if 'change_password' in request.POST :
            old_pwd = request.POST ["old_password"]
            new_pwd = request.POST ["new_password"]
            sellerid = request.session["sellerid"] 
            # seller = Seller.objects.filter(id = sellerid)               #get can't be used ,instead use filter while using update
            # for i in seller :                                           #use loop while filtering
            #  if (i.s_password == old_pwd):
            #   seller.update(s_password = new_pwd)                         #updating password
            
            
            seller=Seller.objects.get(id = sellerid)                      #another method using get ,
            if (seller.s_password == old_pwd) :
                seller.s_password = new_pwd
                seller.save()
            else :
                msg = 'Enter valid password'
                return render (request,'seller/change_password.html',{'msg':msg})              #redirect - passing url
               
              

    return render (request,'seller/change_password.html')
    
def catalogue(request):
    products = Product.objects.filter(seller = request.session ['sellerid'])
    return render(request,'seller/product_catalogue.html',{"products" :products})

def add_product(request):
    msg = ''
    if request.method == 'POST' :
        if 'add_product' in request.POST :
            p_name = request.POST["product_name"]
            p_number =int(request.POST["product_number"])
            p_details = request.POST["product_details"]
            p_price = int (request.POST["product_price"])                      #convert integer -int()
            p_stock = request.POST["product_stock"]
            p_image = request.FILES["product_image"]
            product = Product (
                prod_name =  p_name,                
                prod_number = p_number,
                prod_details = p_details,
                prod_price = p_price,
                prod_stock =  p_stock,
                prod_image =   p_image,
                seller_id = request.session ['sellerid']                   #setting foreignkey
            )
            product.save()
            msg = 'Successfully added product'

    return render (request,'seller/add_product.html',{'msg':msg})   

def stock_update(request):
    return render (request,'seller/stock_update.html')     

# def catalogue (request):
#     product = Product.objects.all()
#     return render(request,'seller/product_catalogue.html',{"products":product})

