from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse
from .models import TempData

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Directly from Django")

def base(request):
    is_object = False
    users = TempData.objects.all()
    #users = TempData.objects.get(id=1)
    # users = TempData.objects.filter(id=2)


    if  isinstance(users, TempData):
        print(users.id, users.name, users.age, users.job)
        is_object = True

    return render(request, 'base.html', {'users': users, 'is_object':is_object})