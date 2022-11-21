from unicodedata import name
from django.urls import path
from . import views

app_name='admin'

urlpatterns=[
    path('home',views.home,name="adminhome"),
]