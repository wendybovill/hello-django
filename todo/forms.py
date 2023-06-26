from django import forms
from .models import Item
from django.test import TestCase


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
