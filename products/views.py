from django.shortcuts import get_object_or_404, render
from . models import Products,Category

# Create your views here.
def category_list(request):
    products=Products.objects.all()
    category=Category.objects.all()
    context={'products':products,'category':category}
    return render(request,'products/category_list.html',context)

def product_list(request,category_slug):
    category=Category.objects.all()
    category1=get_object_or_404(Category,slug=category_slug)
    products1=Products.objects.filter(category=category1)
    context={'category1':category1,'products1':products1,'category':category}
    return render(request,'products/product_list.html',context)
