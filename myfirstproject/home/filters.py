import django_filters
from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields ='__all__'
        exclude=['customer','date_created']


class itemsFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields ='__all__'
        exclude=['pic','tags','date_created','price','source']
        
       
       


