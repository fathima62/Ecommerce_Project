from django.shortcuts import render
from rest_framework.response import Response
from common.models import Customer
from rest_framework.decorators import api_view
from .serializer import CustomerSerializer
from django.http import JsonResponse
from django.http import HttpResponse
import logging
logger = logging.getLogger('django')

# Create your views here.

@api_view(['GET'])
def load_customer (request) :
    customer = Customer.objects.all()
    serialized_data = CustomerSerializer(customer,many = True)
    logger.info("this is info message")
    return JsonResponse (serialized_data.data,safe = False)


@api_view (['POST'])
def add_custmer (request) :
    serialized_data = CustomerSerializer (data = request.data)
    if serialized_data.is_valid() :
        serialized_data.save()
        return JsonResponse ({'message' : "Customer is registered successfully"})
    else :
        print ("Form is not valid") 
        # return JsonResponse ({" error"})   


@api_view (['PUT'])
def update_customer (request,id) :
    customer = Customer.objects.get(id = id)
    serialized_data = CustomerSerializer (customer,data = request.data)
    if serialized_data.is_valid() :
        serialized_data.save ()
        return JsonResponse ({'message' : "Customer is updated successfully"})
    else :
        return JsonResponse ({'message' : "Customer is not updated"})   


@api_view (['DELETE'])
def delete_customer (request,id) :
    customer = Customer.objects.get(id = id)
    customer.delete()
    return JsonResponse ({"message" : "customer is deleted"})

@api_view (['GET'])
def index (request) :
    message = "congrats,you created an API"
    return Response(message)

@api_view (['GET']) 
def num (request) :
    num = 5
    return Response (num)


      



