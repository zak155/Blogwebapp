from django.shortcuts import redirect, render

from blogs.models import Blog, Category

def home(request):
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    post=Blog.objects.filter(is_featured=False,status='Published')
    context={
        'categories':categories,
        'featured_posts':featured_post,
        'posts':post,
    }
    return render(request,'home.html',context)