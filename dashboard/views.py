from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blogs.models import Blog, Category
from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify

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
    
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts
    } 
    return render(request,'dashboard/posts.html',context)   
def add_post(request):
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' +str(post.id)
            post.save()
            return redirect('posts')
        
    else:
        form=BlogPostForm()
    return render(request,'dashboard/add_post.html', {'form': form})

def edit_post(request,id):
    post=get_object_or_404(Blog, id=id)
    if request.method=='POST':
        form=BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' +str(post.id)
            return redirect('posts')
    else:
        form=BlogPostForm(instance=form)
    return render(request,'dashboard/edit_post.html', {'form': form})

def delete_post(request,id):
    post=get_object_or_404(Blog, id=id)
    if request.method=='POST':
        post.delete()
        return redirect('posts')

def users(request):
    user=User.objects.all()
    context={
        'users':user
    }
    return render(request,'dashboard/users.html',context)   
def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('users')
    form=AddUserForm
    context={
        'form':form
    }
    return render(request,'dashboard/add_user.html',context)
def edit_user(request,pk):
    user=get_object_or_404(User,pk)
    if request.method=='POST':
        form=EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
    form=EditUserForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/edit_user.html',context)    
def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk) 
    if request.method=='POST':
        user.delete()
        return redirect('user')
              