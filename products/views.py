from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.contrib import messages
from django.views import generic

from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def listProduct(request):
    products = Product.objects.order_by('complete')
    context = {
                'object': products
            }
    return render(request, 'products_func/product-list.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    context = {'form':form}
    return render(request, 'products_func/product-create.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method =='POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    context = {'form':form}
    return render(request, 'products_func/product-update.html', context)

def detailProduct(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'object':product}
    return render(request, 'products_func/product-detail.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products:list')

    context = {'object':product}
    return render(request, 'products_func/product-delete.html', context)



