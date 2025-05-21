# Create your views here.
from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'inventory/home.html', {'items': items})
