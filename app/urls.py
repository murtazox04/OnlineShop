from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    # path('search', ProductListView.as_view(), name='search'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('register/', RegisterView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='products'),
    path('men-products/', MenProductView.as_view(), name='men-products'),
    path('women-products/', WomenProductView.as_view(), name='women-products'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('single/<int:id>', SingleView.as_view(), name='single'),
    path('edit-product/<int:id>/', ProductUpdateView.as_view(), name='edit-product'),
    path('delete-product/<int:id>/', ProductDeleteView.as_view(), name='delete-product'),
    path('edit-product/', ProductCreateView.as_view(), name='add-product'),
]
