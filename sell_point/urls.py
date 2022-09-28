from django.urls import path, include



urlpatterns = [
    path('', include('providers.urls')),
    path('', include('accounts.urls')),
    path('', include('employes.urls')),
    path('', include('category.urls')),
    path('', include('products.urls')),
    path('', include('locals.urls')),
]
