from .models import shop, product, category
from django import forms

class ShopRegister(forms.ModelForm):
    class Meta:
        model = shop
        fields = "__all__"

class ProductRegister(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"
    
class CategoryRegister(forms.ModelForm):
    class Meta:
        model = category
        fields = "__all__"
        
class changeshop(forms.ModelForm):
    class Meta:
        model = shop
        exclude = ['id']
    
class changeproduct(forms.ModelForm):
    class Meta:
        model = product
        exclude = ['id']

class changecategory(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'