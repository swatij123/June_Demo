from enum import member

from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import ClientContact
from .forms import client
from .forms import clientContact
from .models import Client
from django.contrib import messages
from django.template import loader
from django.shortcuts import HttpResponse
import pandas as pd
from django.urls import reverse

#def home(request):
   # return render(request, 'client/home.html')

def AddClient(request):
   
    if request.method == "POST":
        form = client(request.POST)
        if form.is_valid():
            form.save()
            Name = form.cleaned_data.get('Name')
            messages.success(request, f'Account Created for the {Name}!')
            return redirect('/home/')    
    else:
        form = client()
    return render(request, 'client/register.html', {'form': form})


def ClientProfile(request):
    if request.method == "POST":
        
        form = clientContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')    
    else:
        form = clientContact()
    return render(request, 'client/profile.html', {'form': form})


def home(request):
    mymembers = Client.objects.all().values()
    template = loader.get_template('client/home.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))

def delete(request, id):
    member = Client.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('home'))

def update(request, id):
  mymember = ClientContact.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def view(request,id):
    clientname=Client.objects.filter(id=id).values()

    member= ClientContact.objects.filter(ClientName_id=id).values()
    print(member)
    print(clientname)
    template = loader.get_template('client/view.html')
    context = {
    'member':member,
    'clientname' :clientname,
  }
    
    return HttpResponse(template.render(context, request))

     #df = pd.DataFrame(list(Client.objects.values('ClientName','Currency','BillingMethod')))
     #geeks_object = df.to_html()
     #return HttpResponse(geeks_object)
# Create your views here.