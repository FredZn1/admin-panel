from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(request, 'categories/category_list.html', ctx)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    ctx = {'category': category}
    return render(request, 'categories/category_detail.html', ctx)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:list')
    else:
        form = CategoryForm()
    ctx =  {'form': form}
    return render(request, 'categories/category_form.html',ctx)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:detail', pk=pk)
    else:
        form = CategoryForm(instance=category)
    ctx = {'form': form}
    return render(request, 'categories/category_form.html', ctx)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    ctx = {'category': category}
    return render(request, 'categories/category_confirm_delete.html', ctx)
