from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import Category, Product


def product_all(request):
    query = request.GET.get('q')
    
    products = Product.products.all()

    if query:
        products = products.filter(Q(title=query) | Q(author=query))
    return render(request, 'store/home.html', {'products': products, 'query': query})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})

