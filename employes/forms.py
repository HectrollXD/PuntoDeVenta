from locals.models import Locals
from .models import Employes
from django import forms



#--------------------------------------------------------------------------------------------------- Add employe form
class AddEmployeFormClass( forms.ModelForm ):
    name = forms.CharField(
        required = True,
        max_length = 128,
        label = 'Name',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    first_lastname = forms.CharField(
        required = True,
        max_length = 128,
        label = 'First last name',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    second_lastname = forms.CharField(
        required = False,
        max_length = 128,
        label = 'Second last name',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    local = forms.ModelChoiceField(
        queryset = Locals.objects.all().order_by('local_name'),
        label = 'Local',
        empty_label = 'Select a local',
        required = True,
        blank = False,
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select',
            }
        )
    )

    class Meta:
        model = Employes
        fields = [
            'name',
            'first_lastname',
            'second_lastname',
            'local',
        ]
