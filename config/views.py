from django.shortcut import render

def home(request):
    return render(request,'home.html')