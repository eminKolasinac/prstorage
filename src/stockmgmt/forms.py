from random import randint, random
from django import forms
from .models import Stock
import random

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name', 'quantity']