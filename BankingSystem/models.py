from unicodedata import name
from django.db import models
from django.forms import model_to_dict

class Customer(models.Model):
    Name=models.CharField('Name',max_length=32)
    Account_Number=models.CharField('Account_Number',max_length=9)
    Balance=models.FloatField('Balance')
    Address=models.CharField('Address',max_length=100)
    Mobile_Number=models.CharField('Mobile_Number',max_length=10)
class Transaction(models.Model):
    Sender=models.CharField('Sender',max_length=32)
    Receiver=models.CharField('Receiver',max_length=32)
    Amount=models.FloatField('Amount')
