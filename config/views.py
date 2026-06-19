from django.contrib import auth
from django.shortcuts import redirect, render
from about.models import About
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    try:
        about=About.objects.get()
    except:
        about=None    
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about
    }
    return render(request,'home.html',context)
def register(request):
    from config.forms import RegisterForm
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=RegisterForm()    
    context={
        'form':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    else:
     form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context) 
def logout(request):
    auth.logout(request)
    return redirect('home')