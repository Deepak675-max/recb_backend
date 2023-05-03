from django import forms
from .models import department
from django.forms import ModelForm, TextInput


class MyForm(forms.ModelForm):
    class Meta:
        model = department
        fields = ["title", "summary", "image", "total_students"]
        labels = {"title": "Name", "summary": "Descryption",
                  "image": "Image", "total_students": "Total student"}
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; margin-bottom:20px',
            }),
            'summary': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
            }),
        }
