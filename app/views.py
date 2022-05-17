from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from app.models import *


class ProductView(ListView):
    model = Product
    template_name = 'blog/index.html'
    context_object_name = 'products'


class SearchResultsView(ListView):
    model = Product
    template_name = 'blog/search-detail.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('search')
        products = Product.objects.filter(Q(name__icontains=query))
        return products


class RegisterView(ListView):
    model = Product
    template_name = 'blog/register.html'
    context_object_name = 'register'


class ProductListView(ListView):
    model = Product
    template_name = 'blog/products.html'
    context_object_name = 'products'
    success_url = '/'


class MenProductView(ListView):
    model = Product
    template_name = 'blog/men_product.html'
    context_object_name = 'men-products'


class WomenProductView(ListView):
    model = Product
    template_name = 'blog/women_product.html'
    context_object_name = 'women-products'


class ContactView(ListView):
    model = Product
    template_name = 'blog/contact.html'
    context_object_name = 'contacts'


class SingleView(ListView):
    model = Product
    template_name = 'blog/single.html'
    context_object_name = 'single'

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs.get('id'))


class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        'mens': MenProduct,
        'womens': WomenProduct
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()

        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'blog/product_detail.html'
    slug_url_kwarg = 'slug'


class ProductCreateView(CreateView):
    model = Product
    fields = ['category', 'name', 'slug', 'description', 'price', 'image']
    template_name = 'blog/edit-product.html'
    context_object_name = 'form'
    success_url = '/product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'authors', 'description',
              'price', 'publisher', 'publication_date', 'image']
    template_name = 'blog/edit-product.html'
    context_object_name = 'form'
    success_url = '/'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products-delete'
    template_name = 'blog/product-delete.html'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs.get('id'))
