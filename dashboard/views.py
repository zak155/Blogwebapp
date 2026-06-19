from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.contrib.auth.decorators import login_required

from blogs.models import Blog, Category
from .forms import CategoryForm

login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blog_count
    }
    return render(request, 'dashboard/dashboard.html',context)
def categoryi(request):
    return render(request,'dashboard/categories.html')
def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    else:
        form=CategoryForm()
    return render(request,'dashboard/add_category.html', {'form': form})
def edit_category(request,id):
    category=get_object_or_404(Category, id=id)
    if request.method=='POST':
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=CategoryForm(instance=category)
    return render(request,'dashboard/edit_category.html', {'form': form})
def delete_category(request,id):
    category=get_object_or_404(Category, id=id)
    if request.method=='POST':
        category.delete()
        return redirect('categories')
   