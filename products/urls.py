from .views import ProductsClassView, EditProductsClassView, DeleteProductClassView
from django.urls import path



urlpatterns = [
    path('products/products/', ProductsClassView.as_view(), name = 'productsUrl'),
    path(
        'products/edit_product/<slug:slugProduct>',
        EditProductsClassView.as_view(),
        name = 'editProductUrl'
    ),
    path(
        'products/delete_product/<slug:slugProduct>',
        DeleteProductClassView.as_view(),
        name = 'deleteProductUrl'
    )
]
