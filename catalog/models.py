from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Unique identifier', max_length=100)
    created = models.DateTimeField('Created on', auto_now_add=True)
    modified = models.DateTimeField('Modified on', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Unique identifier', max_length=100)
    created = models.DateTimeField('Created on', auto_now_add=True)
    modified = models.DateTimeField('Modified on', auto_now=True)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)

    category = models.ForeignKey(Category, verbose_name='Category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})