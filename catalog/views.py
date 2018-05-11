from django.shortcuts import render
from catalog.models import Category, Product


# def product_list(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, 'product/product_list.html', context)

def catalog_list(request):
    context = {
        'product_list': Category.objects.all()
    }
    return render(request, 'product/product_list.html', context)


def category(request, slug):
    categ = Category.objects.get(slug=slug)  # Pega pelo nome passado na URL
    context = {
        'current_category': categ,
        'product_list': Product.objects.filter(category=categ),
    }
    return render(request, 'product/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)