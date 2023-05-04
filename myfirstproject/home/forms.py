from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Customer


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ='__all__'


class CreateUserForm(ModelForm):
    class Meta:
         model = Customer
         fields='__all__'


