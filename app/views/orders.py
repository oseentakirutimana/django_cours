from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Order,Category,Product
from app.forms import OrderForm
from django.contrib import messages

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    Orders = Order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'Orders': Orders
        }
    )

def create(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = OrderForm()
    return render(
        request,
        'app/orders/create.html',
        {
            'form': form,
            'categories':categories
        }
    )

def store(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"  ")
        return redirect('/orders')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
        else:
            Orders = Order.objects.get(pk=id)
            form = OrderForm(instance=Orders)
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
            Orders = Order.objects.get(pk=id)
            form = OrderForm(request.POST,instance=Orders)
        if form.is_valid():
            form.save()
            messages.success(request," Modification du commande avec succe ")
        return redirect('/orders')
def delete(request, id):
    Orders = Order.objects.get(pk=id)
    Orders.delete()
    messages.success(request," Suppression du commande avec succe ")
    return redirect('/orders')

def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/orders/getProducts.html',
        {
            'products': products
        }
    )
    
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk = id_product)
    return render(
        request,
        'app/orders/getUnitPrice.html',
        {
            'product': product
        }
    )