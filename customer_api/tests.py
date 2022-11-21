from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.

class TestSample (TestCase) :
    def setup(self) :
       self.client = APIClient

    def test_index(self) :                                        # shoul start with test keyword
        url = reverse('customer_api:index')                                   # url - to get url pattern using name attribute
        res = self.client.get(url)                                # to get response from the corresponding url (here response will be the message)
        # here res.data contains message
        self.assertEquals (res.data,"congrats,you created an API")   #self.assertequals method compares two strings
        
    
    def test_num (self) :
        url = reverse ("customer_api:num")
        res = self.client.get(url)
        self.assertEquals (res.data,8) 
