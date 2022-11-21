from .import views
from django.urls import path

app_name = "seller_api"
urlpatterns = [ 
    path ('load_seller',views.load_seller,name="load_seller"),
    path ('add_seller',views.add_seller,name="add_seller"),
    path('upload_image',views.upload_image,name = "upload_image")
]

