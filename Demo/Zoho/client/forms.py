from msilib.schema import tables
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, ClientContact

class clientContact(forms.ModelForm):
    class Meta:
        model = ClientContact
        fields = ['ClientName','Emailid','FirstName','LastName','Phone','Mobile','Fax']
        

class client(forms.ModelForm):
    class Meta:
        model =Client
        fields = ['ClientName','Currency','BillingMethod']


