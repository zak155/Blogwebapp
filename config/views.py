from django.shortcuts import redirect, render

from blogs.models import Blog, Category

def home(request):
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True).first()
    context={
        'categories':categories
    }
    return render(request,'home.html',context)