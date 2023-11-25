from django.urls import path
from .views import shop, product, category, changeshop, changeproduct, changecategory, activeproduct, notactiveproduct
from django import views

urlpatterns=[
    path('',shop),
    path('product', product),
    path('category',category),
    path('changeshop',changeshop),
    path('changeproduct',changeproduct),
    path('changecategory',changecategory),
    path('activeproduct',activeproduct),
    path('notactiveproduct',notactiveproduct)
]