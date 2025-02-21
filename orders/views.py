from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.objects.all()
    ctx = {'orders': orders}
    return render(request, 'orders/list.html', ctx)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    ctx = {'order': order}
    return render(request, 'orders/detail.html', ctx)

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:list')
    else:
        form = OrderForm()
    ctx = {'form': form}
    return render(request, 'orders/form.html', ctx)

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:detail', pk=pk)
    else:
        form = OrderForm(instance=order)
    ctx = {'form': form}
    return render(request, 'orders/form.html', ctx)

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:list')
    ctx = {'order': order}
    return render(request, 'orders/list.html', ctx)
