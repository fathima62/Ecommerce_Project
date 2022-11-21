from django.shortcuts import render
from rest_framework.response import Response
from common.models import Seller
from rest_framework.decorators import api_view
from .serializer import SellerSerializer
from django.http import JsonResponse
from seller.models import Product

# Create your views here.


@api_view (['GET'])
def load_seller (request) :
    seller = Seller.objects.all()
    serialized_info = SellerSerializer(seller,many = True)                        #many = true means that queryset contains multiple objects.
    return JsonResponse (serialized_info.data,safe = False)                  #safe = false to accept python data type 

@api_view (['POST'])
def add_seller(request) :
    serialized_info = SellerSerializer(data = request.data)
    if serialized_info.is_valid() :
        serialized_info.save()
        return JsonResponse ({"message" : "seller is added successfully"})
    else :
        print ("Form is not valid")   

@api_view (['POST']) 
def upload_image (request,p_id) :
    product = Product.objects.get(id = p_id)
    product.image = request.FILES.get(['image'])
    product.save()
    return Response ('Image was uploaded')


