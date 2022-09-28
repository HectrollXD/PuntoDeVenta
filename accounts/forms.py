from django.contrib.auth.models import Group
from employes.models import Employes
from users.models import Users
from django import forms



#--------------------------------------------------------------------------------------------------- Login form
class LoginFormClass( forms.Form ):
    username = forms.CharField(
        required = True,
        disabled = False,
        max_length = 32,
        label = 'Username',
        help_text = 'Enter your username',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        required = True,
        disabled = False,
        max_length = 32,
        label = 'Password',
        help_text = 'Enter your password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )


#--------------------------------------------------------------------------------------------------- Create group
class CreateGroupFormClass( forms.ModelForm ):
    name = forms.CharField(
        required = True,
        label = 'Group name',
        disabled = False,
        max_length = '150',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Group
        fields = '__all__'



#--------------------------------------------------------------------------------------------------- Account form
class CreateAccountFormClass( forms.ModelForm ):
    group = forms.ModelChoiceField(
        queryset = Group.objects.all().order_by('name'),
        label = 'User group',
        empty_label = 'Select a user group',
        required = True,
        blank = False,
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select',
            }
        )
    )
    username = forms.CharField(
        required = True,
        max_length = 32,
        label = 'Username',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required = True,
        max_length = 256,
        label = 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        required = True,
        max_length = 32,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    confirm_password = forms.CharField(
        required = True,
        max_length = 32,
        label = 'Confirm password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Users
        fields = [
            'group',
            'username',
            'email',
            'password',
            'confirm_password',
        ]

    def clean(self):
        super(CreateAccountFormClass, self).clean()
        passwds = {
            'pass': self.cleaned_data.get('password'),
            'cpass': self.cleaned_data.get('confirm_password')
        }
        if passwds['pass'] != passwds['cpass']:
            self._errors['confirm_password'] = self.error_class(
                ['The password confirmation is not equal to the entered password.']
            )
        return self.cleaned_data



#--------------------------------------------------------------------------------------------------- Search user
class SearchUserFormClass( forms.Form ):
    username = forms.CharField(
        required = False,
        label = 'Username',
        disabled = False,
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    name = forms.CharField(
        required = False,
        label = 'Name',
        disabled = False,
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    first_lastname = forms.CharField(
        required = False,
        label = 'First last name',
        disabled = False,
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    second_lastname = forms.CharField(
        required = False,
        label = 'Second last name',
        disabled = False,
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    group = forms.ModelChoiceField(
        queryset = Group.objects.all().order_by('name'),
        label = 'User group',
        empty_label = 'Select a user group',
        required = False,
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select',
            }
        )
    )

    class Meta:
        fields = '__all__'



#--------------------------------------------------------------------------------------------------- Configure User
class ConfigUserFormClass( forms.ModelForm ):
    profile_image_name = forms.ImageField(
        required = False,
        max_length = 256,
        label = 'Select image',
        widget = forms.FileInput(
            attrs = {
                'style': 'display: none;',
            }
        )
    )
    telephone_number = forms.CharField(
        required = False,
        max_length = 10,
        label = 'Office telephone number',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    extension = forms.CharField(
        required = False,
        max_length = 8,
        label = 'Exension',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required = False,
        max_length = 256,
        label = 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Users
        fields = [
            'profile_image',
            'telephone_number',
            'extension',
            'email',
        ]
    
    

#--------------------------------------------------------------------------------------------------- Configure Employe
class ConfigEmployeFormClass( forms.ModelForm ):
    name = forms.CharField(
        required = False,
        max_length = 128,
        label = 'Name',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    first_lastname = forms.CharField(
        required = False,
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

    class Meta:
        model = Employes
        fields = [
            'name',
            'first_lastname',
            'second_lastname',
        ]



#--------------------------------------------------------------------------------------------------- Configure password
class ConfigPasswordFormClass( forms.ModelForm ):
    password = forms.CharField(
        required = False,
        max_length = 32,
        label = 'Current password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    new_password = forms.CharField(
        required = False,
        max_length = 32,
        label = 'New password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    confirm_new_password = forms.CharField(
        required = False,
        max_length = 32,
        label = 'Confirm password',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Users
        fields = [
            'password',
            'new_password',
            'confirm_new_password'
        ]



#--------------------------------------------------------------------------------------------------- Edit Account
class EditAccountFormClass( forms.ModelForm ):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    group = forms.ModelChoiceField(
        queryset = Group.objects.all().order_by('name'),
        required = True,
        label = 'User group',
        widget = forms.Select(
            attrs = {
                'class': 'form-control form-select',
            }
        )
    )

    class Meta:
        model = Users
        fields = [
            'username',
            'group',
        ]

    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group', None)
        super(EditAccountFormClass, self).__init__(*args, **kwargs)
        if group:
            self.fields['group'].initial = group
