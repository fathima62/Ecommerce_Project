from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Seller(models.Model):
    s_name = models.CharField(max_length = 20)
    s_email = models.CharField (max_length = 70)
    s_phone = models.BigIntegerField ()
    s_Address = models.CharField (max_length = 300)
    s_accnumber = models.BigIntegerField ()
    s_ifsc = models.CharField(max_length = 70)
    s_accholdername = models.CharField(max_length = 20)
    s_password = models.CharField(max_length = 8,default='')
    s_pic = models.ImageField(upload_to = "seller/",default='')

class Customer(models.Model) :
    c_firstname = models.CharField(max_length = 20,default='')
    c_secondname =  models.CharField(max_length = 20)
    c_email = models.CharField (max_length = 70)
    c_phone = models.BigIntegerField ()
    c_Address = models.CharField (max_length = 300)
    c_password = models.CharField(max_length = 8)