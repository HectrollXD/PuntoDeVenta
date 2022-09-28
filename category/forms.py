from .models import Categories
from django import forms



#--------------------------------------------------------------------------------------------------- Add categories
class AddNewCategoryFormClass( forms.ModelForm ):
    category_name = forms.CharField(
        required = True,
        label = 'Category name',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Categories
        fields = [
            'category_name'
        ]



#--------------------------------------------------------------------------------------------------- Search categories
class SearchCategoriesFormClass( forms.Form ):
    category_name = forms.CharField(
        required = True,
        label = 'Category name',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        fields = '__all__'