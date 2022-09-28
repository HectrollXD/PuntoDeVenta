from itertools import product
from.forms import AddNewProductFormClass, SearchProductFormClass
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins import GroupRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Products
from app import getAppName



#--------------------------------------------------------------------------------------------------- Products view
class ProductsClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2, 3]
    template_name = 'products.html'
    queryset = None
    form_class = {
        'searchForm': SearchProductFormClass,
        'addForm': AddNewProductFormClass,
    }
    
    def get(self, request):
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Products',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )
    
    def post(self, request):
        form = self.form_class['addForm'](request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The product has been saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to save the product.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('productsUrl')



#--------------------------------------------------------------------------------------------------- Edit products
class EditProductsClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]
    template_name = 'products.html'
    queryset = None
    form_class = {
        'searchForm': SearchProductFormClass,
    }

    def get(self, request, slugProduct):
        product = get_object_or_404(Products, product_alias = slugProduct)
        self.form_class['addForm'] = AddNewProductFormClass(instance = product)
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Products',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def post(self, request, slugProduct):
        product = get_object_or_404(Products, product_alias = slugProduct)
        form = AddNewProductFormClass(request.POST or None, instance = product)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The product has been updated successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to update the product.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('productsUrl')



#--------------------------------------------------------------------------------------------------- Delete products
class DeleteProductClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]

    def get(self, request, slugProduct):
        product = get_object_or_404(Products, category_alias = slugProduct)
        try:
            product.delete()
            messages.success(request, 'The product was deleted successfully.')
        except:
            messages.error(request, 'An error was occured while try to delete the product.')
        return redirect('productsUrl')



#--------------------------------------------------------------------------------------------------- Fucntion to set queryset
def setQuery(request):
    query = Products.objects.select_related('category', 'provider')
    searches = getSearch(request)
    if searches['product_code']:
        query = query.filter(product_code = searches['product_code'])
    if searches['product_name']:
        query = query.filter(product_name__icontains = searches['product_name'])
    if searches['product_description']:
        query = query.filter(product_description__icontains = searches['product_description'])
    if searches['category']:
        query = query.filter(category__id = searches['category'])
    if searches['provider']:
        query = query.filter(provider__id = searches['provider'])
    query = query.order_by('product_name')
    return query



#--------------------------------------------------------------------------------------------------- Fucntion to get searches
def getSearch(request):
    searches = {
        'product_code': request.GET.get('product_code'),
        'product_name': request.GET.get('product_name'),
        'product_description': request.GET.get('product_description'),
        'category': request.GET.get('category'),
        'provider': request.GET.get('provider'),
    }
    return searches