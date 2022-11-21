from dataclasses import fields
from pyexpat import model
from common.models import Seller
from rest_framework import serializers

class SellerSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Seller
        fields = "__all__"