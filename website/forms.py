# este archivo se llama forms.py
from .models import Client
from django import forms


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "phone", "state", "city"]
