
from django.http import JsonResponse
from ast import Pass
import email
from django.shortcuts import redirect ,render 
from . models import Customer, Seller
# Create your views here.
def customer_signup(request):
    return render(request,'common/customer_signup.html')
    
def home(request): 
    if request.method == "POST" :
        if 's_signup' in request.POST :
            seller_name = request.POST ["seller_name"]
            seller_email =  request.POST ["email"]
            seller_phone = request.POST ["phone"]
            seller_address = request.POST ["address"]
            seller_accountno = request.POST["account_number"]
            seller_ifsc = request.POST["IFSC"]
            seller_accholder = request.POST["account_holder"]
            seller_password = request.POST["password"]
            seller_image = request.FILES["image"]
            obj = Seller(s_name = seller_name,
            s_email = seller_email,
            s_phone = seller_phone,
            s_Address = seller_address,
            s_accnumber = seller_accountno,
            s_ifsc = seller_ifsc ,
            s_accholdername = seller_accholder ,
            s_password = seller_password,s_pic = seller_image)
            obj.save()


        if 's_login' in request.POST :
            seller_email = request.POST ["email"]  
            seller_password = request.POST ["password"] 
            data_exist = Seller.objects.filter(s_email = seller_email , s_password = seller_password).exists()
            if data_exist :
                seller = Seller.objects.get(s_email = seller_email , s_password = seller_password) 
                request.session ['sellerid'] = seller.id
                return redirect ('seller:home')

    if request.method == "POST" :
        if 'c_signup' in request.POST :
            customer_firstname = request.POST ["first_name"]
            customer_secondname = request.POST ["second_name"]
            customer_email = request.POST ["email"]
            customer_phone = request.POST ["phone"]
            customer_address = request.POST ["address"]
            customer_password = request.POST ["password"]
            obj_customer = Customer(
                c_firstname = customer_firstname ,
                c_secondname = customer_secondname,
                c_email = customer_email,
                c_phone = customer_phone,
                c_Address =  customer_address,
                c_password =  customer_password  
            )
            obj_customer.save()

    if 'c_login' in request.POST :
        customer_email = request.POST ["email"]  #name in form
        customer_password = request.POST ["password"]
        data_exist = Customer.objects.filter(c_email= customer_email ,c_password = customer_password).exists()   #model = variable name ,to crosscheck the login data
        if data_exist :
            customer = Customer.objects.get(c_email= customer_email ,c_password = customer_password)
            request.session ['userid'] = customer.id     # pass session key to the browser cookies
            request.session ['username'] = customer.c_firstname
            return redirect ('customer:customerhome')     #customerhome is the name in urlpattern


      

    return render(request,'common/home.html')

def email_exist (request) :
    email = request.POST["email"]                                             #email is the key
    email_exists = Customer.objects.filter( c_email = email).exists()
    return JsonResponse ({'status' : email_exists})


def s_email_exist (request) :
    s_email = request.POST ["s_email"]
    s_email_exists = Seller.objects.filter (s_email = s_email).exists()
    return JsonResponse ({"status":s_email_exists})


# def home2(request): 
#     return render(request,'common/home2.html')