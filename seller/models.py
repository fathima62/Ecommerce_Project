from distutils.command.upload import upload
from email.policy import default
from itertools import product
from math import prod
from django.db import models
from common.models import Seller

# Create your models here.
class Product (models.Model) :
    prod_name = models.CharField(max_length = 70)
    seller = models.ForeignKey (Seller,on_delete=models.CASCADE)
    prod_number = models.BigIntegerField()
    prod_details = models.CharField (max_length = 400)
    prod_price = models.BigIntegerField()
    prod_stock = models.BigIntegerField()
    prod_image = models.ImageField (upload_to = 'product/')
    