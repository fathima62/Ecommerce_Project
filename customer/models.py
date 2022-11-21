from itertools import product
from django.db import models
from common.models import Customer
import datetime
from seller.models import Product

# Create your models here.

class Cart (models.Model) :
    product= models.ForeignKey (Product,on_delete=models.CASCADE)
    customer = models.ForeignKey (Customer,on_delete =models.CASCADE )
    quantity = models.IntegerField ()


class Order (models.Model) :
    product = models.ForeignKey (Product,on_delete = models.CASCADE)
    customer = models.ForeignKey (Customer,on_delete = models.CASCADE)
    quantity = models.IntegerField ()
    address = models.CharField (max_length = 300)
    phone = models.BigIntegerField()
    date = models.DateField (default = datetime.datetime.today)
    status = models.BooleanField (default = False)