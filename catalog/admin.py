from django.contrib import admin
from catalog.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']  # Lista estas colunas no Admin
    search_fields = ['name', 'slug']  # Cria o campo de pesquisa dentro do Admin
    list_filter = ['created', 'modified']  # Cria o campo de filtro dentro do Admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']  # Lista estas colunas no Admin
    search_fields = ['name', 'slug', 'category__name']  # Cria o campo de pesquisa dentro do Admin
    list_filter = ['created', 'modified']  # Cria o campo de filtro dentro do Admin


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)