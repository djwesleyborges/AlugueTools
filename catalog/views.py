from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalog.models import Category, Product

# Lista todas categorias(catalog)
class CatalogListView(generic.ListView):
    model = Category
    template_name = 'product/product_list.html'
    # context_object_name = 'products' # usar somente caso queira mudar o nome da variavel na renderização do template


catalog_list = CatalogListView.as_view()
'''
def catalog_list(request):
    context = {
        'product_list': Category.objects.all()
    }
    return render(request, 'product/product_list.html', context)
'''

class CategoryListView(generic.ListView):
    template_name = 'product/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()

'''
def category(request, slug):
    categ = Category.objects.get(slug=slug)  # Pega pelo nome passado na URL
    context = {
        'current_category': categ,
        'product_list': Product.objects.filter(category=categ),
    }
    return render(request, 'product/category.html', context)
'''

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)