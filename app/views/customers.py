from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Customer
from app.forms import CustomerForm

def index(request):
    assert isinstance(request, HttpRequest)
    customers = Customer.objects.all()
    return render(
        request,
        'app/customers/index.html',
        {
            'customers': customers
        }
    )
    
def create(request):
    form = CustomerForm()
    return render(
        request, 
        'app/customers/create.html',
        {
            'form': form
        }
    )
    
def save(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customers')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/customers')
    
def delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customers')