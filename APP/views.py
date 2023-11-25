from django.shortcuts import render
from django.http import HttpResponse
from . import form
from .models import shop, product, category

def shop(request):
    if 'q' in request.GET:
        q = request.GET['q']       
        shop = shop.objects.filter(title__icontains=q)

    else:
        shop = shop.objects.all()
    context = {'shop':shop,}

    return render(request,'/shop.html',context)

def product(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        products = product.objects.filter(id__icontains=q)
    
    else:
        products = product.objects.all()

    context = {'products':products}

    return render(request,'/products.html',context)

def category(request):
    if 'q' in request.GET:
        q = request.GET['q']
        category = Category.objects.filter(title__icontains=q)
        

    else:
        category = Category.objects.all() 
        
    
    
    context = {'category':category}
    return render(request,'/category.html',context)

def changeshop(request,id):
    if request.method=='POST':
        pi = Shop.objects.get(pk=id)
        form = ShopUpdate(request.POST,request.FILES,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        pi = Shop.objects.get(pk=id)
        form = ShopUpdate(instance=pi)   
    context = {'form':form,'id':id}
    return render(request,'/changehop.html',context)


def changeproduct(request,id):
    if request.method=='POST':
        pi = Product.objects.get(pk=id)
        form = ProductUpdate(request.POST,request.FILES,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        pi = Product.objects.get(pk=id)
        form = ProductUpdate(instance=pi)   
    context = {'form':form,'id':id,'img':pi}
    return render(request,'/changeproduct.html',context)

def changecategory(request,id):
    if request.method=='POST':
        pi = Category.objects.get(pk=id)
        form = CategoryUpdate(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        pi = category.objects.get(pk=id)
        form = categoryUpdate(instance=pi)   
    context = {'form':form,'id':id}
    return render(request,'/changecategory.html',context)


def activeproduct(request):
    products = product.objects.filter(active=True)
    return render(request,'/activeproduct.html',{'products':products})

def notactiveproduct(request):
    products = product.objects.filter(active=False)
    return render(request,'/notactiveproduct.html',{'products':products})