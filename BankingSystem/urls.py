from tokenize import Name
from django.urls import path
from . import views
from .models import Customer
data= Customer.objects.all()
urlpatterns=[]
urlpatterns.append(path('home/Customers/<data>',views.customer_Details))
urlpatterns.append(path('',views.home))
urlpatterns.append(path('home/Customers',views.all_Customers,name='all_Customers'))
urlpatterns.append(path('Transfer/',views.transfer,name='transfer'))
urlpatterns.append(path('home/Transactions',views.Transactions))