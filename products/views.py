from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def home(request):
    teachers = Product.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'index.html', ctx)

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'products/product_list.html', ctx)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request, 'products/product_detail.html', ctx)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductForm()
    ctx = {'form': form}
    return render(request, 'products/product_form.html', ctx)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    ctx = {'form': form}
    return render(request, 'products/product_form.html', ctx)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list')
    ctx = {'product': product}
    return render(request, 'products/product_confirm_delete.html', ctx)
