from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from .forms import StockCreateForm

# Create your views here.
def home(request):
    title = "Welcome to your Home Page"
    context = {
        "title": title,   #varijabila koju pozivamo u html fajlu
    }
    return render(request, "home.html",context)  #renderovanje

def list_items(request):
    title = "List of list_items"
    queryset = Stock.objects.all()
    context = {
        "title": title,   #varijabila koju pozivamo u html fajlu
        "queryset": queryset,
    }
    return render(request, "list_items.html",context)  #renderovanje

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid() and form:
        form.save()
        return redirect(list_items)
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)