from django.db import models
from django.contrib.auth.models import User
import django_tables2 as tables


class Client(models.Model):
    
    ClientName= models.CharField(max_length=200, blank=True)
    Currency = models.CharField(max_length=20, blank=True)
    BillingMethod = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.ClientName

class ClientContact(models.Model):
 
  ClientName = models.ForeignKey(Client, on_delete=models.CASCADE)
  Emailid = models.CharField(max_length=200, blank=True)
  FirstName = models.CharField(max_length=200, blank=True)
  LastName = models.CharField(max_length=200, blank=True)
  Phone = models.SmallIntegerField()
  Mobile = models.SmallIntegerField()
  Fax = models.CharField(max_length=200, blank=True)

  def __str__(self):
        return self.ClientName
  
        



# Create your models here.
