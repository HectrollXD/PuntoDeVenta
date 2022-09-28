from .models import Providers
from django import forms



#--------------------------------------------------------------------------------------------------- Add provider
class AddNewProviderFormClass( forms.ModelForm ):
    provider_name = forms.CharField(
        required = True,
        label = 'Provider name',
        max_length = 128,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Providers
        fields = [
            'provider_name'
        ]



#--------------------------------------------------------------------------------------------------- Search provider
class SearchProvidersFormClass( forms.Form ):
    provider_name = forms.CharField(
        required = True,
        label = 'Provider name',
        max_length = 128,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        fields = '__all__'