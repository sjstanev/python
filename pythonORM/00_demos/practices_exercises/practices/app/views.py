from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse
from .models import TempData

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Directly from Django")

def base(request):
    name = "some_variable"
    # users = TempData.objects.all()
    users = TempData.objects.filter(id=2)
    print(users)
    return render(request, 'base.html', {'name': name, 'users': users})