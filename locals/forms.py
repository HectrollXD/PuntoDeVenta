from .models import Locals
from django import forms



#--------------------------------------------------------------------------------------------------- Search locals forms
class SearchLocalFormClass( forms.Form ):
    local_name = forms.CharField(
        required = False,
        label = 'Local name',
        max_length = 128,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    city = forms.CharField(
        required = False,
        label = 'City',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    state = forms.CharField(
        required = False,
        label = 'State',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        fields = '__all__'



#--------------------------------------------------------------------------------------------------- Add new local
class AddNewLocalFormClass( forms.ModelForm ):
    local_name = forms.CharField(
        required = True,
        label = 'Local name',
        max_length = 128,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    street = forms.CharField(
        required = True,
        label = 'Street',
        max_length = 128,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    number = forms.CharField(
        required = True,
        label = 'Number',
        max_length = 16,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    postal_code = forms.CharField(
        required = True,
        label = 'Postal code',
        max_length = 8,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    city = forms.CharField(
        required = True,
        label = 'City',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    state = forms.CharField(
        required = True,
        label = 'State',
        max_length = 64,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Locals
        fields = [
            'local_name',
            'street',
            'number',
            'postal_code',
            'city',
            'state',
        ]
