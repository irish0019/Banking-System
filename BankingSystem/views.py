from cmath import log
from email.headerregistry import Address
from http import client
from pickle import GET
from tokenize import Name
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer,Transaction
def home(request):
    return render(request,'index.html')
def all_Customers(request):
    data=Customer.objects.all()
    return render(request,'Customer.html',{'data':data})
def customer_Details(request,data):
    Memory=Customer.objects.all()
    client_list=[]
    for i in Memory:
        if i.Name==data:
            client=i
        else:
            client_list.append(i)
    return render(request,'View_Customer.html',{'data':client,'list':client_list})
def transfer(request):
    Memory=Customer.objects.all()
    To=request.POST.get('acc_holder')
    From=request.POST.get('from')
    From_Address=request.POST.get('sender')
    Money=float(request.POST.get('amount'))
    reciver_Account=request.POST.get('account')
    x=0
    y=0
    if request.method=="POST":
        for i in Memory:
            if i.Name==To and i.Account_Number==reciver_Account:
                x=1
                reciver=i
            elif i.Name==From and i.Account_Number==From_Address:
                y=1
                client=i
        if x==1 and y==1:
            client_Balance=client.Balance-Money
            reciver_Balance=reciver.Balance + Money
            data1=Customer(id=client.id,Name=client.Name,Account_Number=client.Account_Number,Balance=client_Balance,Address=client.Address,Mobile_Number=client.Mobile_Number)
            data2=Customer(id=reciver.id,Name=reciver.Name,Account_Number=reciver.Account_Number,Balance=reciver_Balance,Address=reciver.Address,Mobile_Number=reciver.Mobile_Number)
            data3=Transaction(Sender=client.Name,Receiver=reciver.Name,Amount=Money)
            data1.save()
            data2.save()
            data3.save()
            response=redirect('http://127.0.0.1:8000/BankingSystem/home/Customers')
            return response
        else:
            return render(request,'transfer.html')
def Transactions(request):
    Memory=Transaction.objects.all()
    return render(request,'Transactions.html',{'data':Memory})
