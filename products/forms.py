from providers.models import Providers
from category.models import Categories
from .models import Products
from django import forms



#--------------------------------------------------------------------------------------------------- Add product form
class AddNewProductFormClass( forms.ModelForm ):
    product_code = forms.CharField(
        required = True,
        label = 'Product code',
        max_length = 16,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    product_name = forms.CharField(
        required = True,
        label = 'Product name',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    product_description = forms.CharField(
        required = False,
        label = 'Description',
        max_length = 256,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    deseable_stock = forms.IntegerField(
        required = True,
        label = 'Deseable stock',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    stock = forms.IntegerField(
        required = True,
        label = 'Stock',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset = Categories.objects.all().order_by('category_name'),
        required = True,
        label = 'Category',
        empty_label = 'Select a category',
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select'
            }
        )
    )
    provider = forms.ModelChoiceField(
        queryset = Providers.objects.all().order_by('provider_name'),
        required = True,
        label = 'Provider',
        empty_label = 'Select a provider',
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select'
            }
        )
    )

    class Meta:
        model = Products
        fields = [
            'product_code',
            'product_name',
            'product_description',
            'deseable_stock',
            'stock',
            'category',
            'provider',
        ]



#--------------------------------------------------------------------------------------------------- Search products
class SearchProductFormClass( forms.Form ):
    product_code = forms.CharField(
        required = False,
        label = 'Product code',
        max_length = 16,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    product_name = forms.CharField(
        required = False,
        label = 'Product name',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    product_description = forms.CharField(
        required = False,
        label = 'Description',
        max_length = 256,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset = Categories.objects.all().order_by('category_name'),
        required = False,
        label = 'Category',
        empty_label = 'Select a category',
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select'
            }
        )
    )
    provider = forms.ModelChoiceField(
        queryset = Providers.objects.all().order_by('provider_name'),
        required = False,
        label = 'Provider',
        empty_label = 'Select a provider',
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select'
            }
        )
    )

    class Meta:
        fields = '__all__'