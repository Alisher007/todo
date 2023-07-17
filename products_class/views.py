from django.shortcuts import render, get_object_or_404
from products.models import Product
from products.forms import ProductForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ProductListView(ListView):
    context_object_name = 'object'
    queryset = Product.objects.order_by('complete')

class ProductDetailView(DetailView):
    queryset = Product.objects.all()

class ProductCreateView(CreateView):
    form_class = ProductForm
    queryset = Product.objects.all() # object_list
    success_url = reverse_lazy('products-class:list' ) # default will redirect to get_absolute_url

    def form_valid(self, form):
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    form_class = ProductForm
    success_url = reverse_lazy('products-class:list' ) # default will redirect to get_absolute_url

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk)

    def form_valid(self, form):
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    success_url = reverse_lazy('products-class:list' ) # default will redirect to get_absolute_url

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk)