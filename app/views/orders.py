from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Order
from app.forms import OrderForm

def index(request):
    assert isinstance(request, HttpRequest)
    Orders = order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': orders
        }
    )
    
def create(request):
    form = OrderForm()
    return render(
        request, 
        'app/orders/create.html',
        {
            'form': form
        }
    )
    
def save(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/orders')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(instance=order)
        return render(
            request,
            'app/orders/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/orders')
    
def delete(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('/orders')