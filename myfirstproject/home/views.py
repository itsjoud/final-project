from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
# from .forms import OrderForm, CreateUserForm
from .forms import OrderForm, CreateUserForm
from .models import *
from .filters import OrderFilter, itemsFilter
# import django.core.mail import send_mail


# Create your views here.
def home(request): # customer dashboard
    return render(request, 'home/home.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        if email == 'admin' and password == '1234':
                return redirect('Admin')
        try:
            customer = Customer.objects.get(email=email, password=password)
            return redirect('home')
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid email or password')
    return render(request, 'signin.html')


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            print(form.errors) # print form errors to console for debugging
    context = {'form':form}
    return render(request,'signup.html',context)

def items(request):    # customer list of items
    items= Product.objects.all()
    myFilter2 = itemsFilter(request.GET, queryset=items)
    items = myFilter2.qs
    
    return render(request, 'home/items.html',{'items':items,"myFilter2":myFilter2})

def customer(request,pk):  # customers list for admin

    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context={"customer": customer, "orders":orders, "order_count":order_count, "myFilter":myFilter}
    return render(request, 'home/customer.html',context)

def Admin(request):   #admin dashboard
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()

    total_orders=orders.count()
    paid=orders.filter(status="Paid").count()
    pending=orders.filter(status="Pending").count()


    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'paid':paid, 'pending':pending}
# 'total_customers':total_customers,
    return render(request, 'home/admin.html', context)

def product(request):  # admin list of items
    product= Product.objects.all()
    myFilter2 = itemsFilter(request.GET, queryset=product)
    product = myFilter2.qs
    return render(request, 'home/adminitems.html',{'product':product,"myFilter2":myFilter2})


def AdmincreateOrder(request,pk):
     OrderFormSet= inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10)
     customer= Customer.objects.get(id=pk)
     formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
     if request.method=="POST":
            formset=OrderFormSet(request.POST, instance=customer)
            if formset.isvalid():
                formset.save()
                return redirect('Admin')
     context={'formset':formset}
     return render(request,'home/admin_order_form.html', context)

def createOrder(request,pk):  #customer order 
     OrderFormSet= inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10)
     customer= Customer.objects.get(id=pk)
     formset=OrderFormSet(queryset=Order.objects.none(), instance=customer)
     if request.method=="POST":
            formset=OrderFormSet(request.POST, instance=customer)
            if formset.isvalid():
                formset.save()
                return redirect('home')
            
     context={'formset':formset}
     return render(request,'home/order_form.html', context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method =='POST':
            form= OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect ('Admin')
    
    context={'form': form}
    return render(request, 'home/admin_order_form.html', context)
    

def delete(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('Admin')
    
    context={"item":order}
    return render(request,'home/delete.html', context)

def contact(request): 
    return render(request, 'home/contact.html')
   