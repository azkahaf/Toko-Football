from django import forms
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-600 bg-gray-700 text-white rounded-md focus:border-blue-400"
            }),
            "price": forms.NumberInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-600 bg-gray-700 text-white rounded-md focus:border-blue-400"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 border border-gray-600 bg-gray-700 text-white rounded-md focus:border-blue-400"
            }),
            "thumbnail": forms.URLInput(attrs={
                "class": "w-full px-4 py-3 border border-gray-600 bg-gray-700 text-white rounded-md focus:border-blue-400"
            }),
            "category": forms.Select(attrs={
                "class": "w-full px-4 py-3 border border-gray-600 bg-gray-700 text-white rounded-md focus:border-blue-400"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "rounded border-gray-600 bg-gray-700 text-blue-600 focus:ring-blue-500"
            }),
        }

        def clean_title(self):
            title = self.cleaned_data["title"]
            return strip_tags(title)

        def clean_content(self):
            content = self.cleaned_data["content"]
            return strip_tags(content)
