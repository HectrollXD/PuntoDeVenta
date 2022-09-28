from .forms import LoginFormClass, CreateAccountFormClass, CreateGroupFormClass, SearchUserFormClass
from .forms import ConfigUserFormClass, ConfigEmployeFormClass, ConfigPasswordFormClass
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from employes.forms import AddEmployeFormClass
from .forms import EditAccountFormClass
from mixins import GroupRequiredMixin
from employes.models import Employes
from django.contrib import messages
from users.models import Users
from django.views import View
from app import getAppName



#--------------------------------------------------------------------------------------------------- Login view
class LoginClassView( View ):
    template_name = 'login.html'
    form_class = LoginFormClass

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('createAccountUrl')
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Login',
                'form': self.form_class,
            }
        )

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user and user.is_deleted == False:
                login(request, user)
                messages.success(request, 'Welcome!')
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('createAccountUrl')
            else:
                messages.error(request, 'Invalid user or password.')
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Login',
                'form': self.form_class,
            }
        )



#--------------------------------------------------------------------------------------------------- Logout
class LogoutClassView(LoginRequiredMixin, View ):
    login_url = 'loginUrl'

    def get(self, request):
        logout(request)
        return redirect('loginUrl')



#--------------------------------------------------------------------------------------------------- Create account
class CreateAcountClassView(LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]
    template_name = 'create_account.html'
    form_class = {
        'accountForm': CreateAccountFormClass,
        'employeForm': AddEmployeFormClass,
        'groupForm': CreateGroupFormClass,
    }

    def get(self, request):
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Create new account',
                'form': self.form_class,
            }
        )

    def post(self, request):
        forms = {
            'accountForm': self.form_class['accountForm'](request.POST or None),
            'employeForm': self.form_class['employeForm'](request.POST or None),
        }
        if forms['accountForm'].is_valid() and forms['employeForm'].is_valid():
            try:
                preSave = forms['accountForm'].save(commit = False)
                preSave.password = make_password(forms['accountForm']['password'].value())
                preSave.save()
                lastUser = Users.objects.latest('id')
                lastUser.groups.add(forms['accountForm'].cleaned_data.get('group'))
                preSave = forms['employeForm'].save(commit = False)
                preSave.user = lastUser
                preSave.save()
                messages.success(request, 'The user was saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to save data.\n')
        else:
            groupForm = self.form_class['groupForm'](request.POST or None)
            if groupForm.is_valid():
                try:
                    groupForm.save()
                    messages.success(request, 'The group has been added successfully.')
                except:
                    messages.error(request, 'An error was ocurred while try save group.')
        return redirect('createAccountUrl')



#--------------------------------------------------------------------------------------------------- Show Accounts
class ShowAllAccountClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]
    template_name = 'show_all_account.html'
    form_class = SearchUserFormClass
    queryset = None

    def get(self, request):
        self.queryset = self.setQueryset()
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Show all accounts',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def setQueryset(self):
        queryset = Users.objects.prefetch_related('employes', 'groups').all().filter(is_deleted = False).exclude(username = self.request.user)
        searches = self.getSearches()
        if searches['username']:
            queryset = queryset.filter(username__icontains = searches['username'])
        if searches['name']:
            queryset = queryset.filter(employes__name__icontains = searches['name'])
        if searches['first_lastname']:
            queryset = queryset.filter(
                employes__first_lastname__icontains = searches['first_lastname']
            )
        if searches['second_lastname']:
            queryset = queryset.filter(
                employes__second_lastname__icontains = searches['second_lastname']
            )
        if searches['group']:
            queryset = queryset.filter(groups = searches['group'])
        queryset = queryset.order_by('employes__name')
        return queryset

    def getSearches(self):
        searches = {
            'username': self.request.GET.get('username'),
            'name': self.request.GET.get('name'),
            'first_lastname': self.request.GET.get('first_lastname'),
            'second_lastname': self.request.GET.get('second_lastname'),
            'group': self.request.GET.get('group'),
        }
        return searches



#--------------------------------------------------------------------------------------------------- Edit Account
class EditAccountClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]
    template_name = 'edit_account.html'
    queryset = None
    form_class = None

    def get(self, request, user):
        self.queryset = get_object_or_404(Users, username = user)
        self.form_class = EditAccountFormClass(instance = self.queryset, group = self.queryset.groups.get().id)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Edit user',
                'form': self.form_class,
                'queryset': self.queryset,
            }
        )

    def post(self, request, user):
        self.queryset = Users.objects.get(username = user)
        self.form_class = EditAccountFormClass(request.POST or None, instance = self.queryset)
        if self.form_class.is_valid():
            try:
                preSave = self.form_class.save(commit = False)
                group = self.queryset.groups.get()
                group.user_set.remove(self.queryset)
                preSave.groups.add(self.form_class.cleaned_data.get('group'))
                preSave.save()
                messages.success(request, 'The user has been update')
            except:
                messages.error(request, 'An erro was ocurred while try to update the user')
        return redirect('showAllAccountsUrl')



#--------------------------------------------------------------------------------------------------- Delete accouunt
class DeleteAccountClassVies( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]

    def get(self, request, userId):
        instance = get_object_or_404(Users, id = userId)
        try:
            instance.is_deleted = True
            instance.save()
            messages.success(request, 'The user has been deleted successfully.')
        except:
            messages.error(request, 'An error was occured while try to delete the user.')
        return redirect('showAllAccountsUrl')




#--------------------------------------------------------------------------------------------------- Configure account
class ConfigureAccountClassView(LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2, 3]
    template_name = 'configure_account.html'
    form_class = None

    def get(self, request, user):
        if user != request.user.username:
            return redirect('configAccountUrl', request.user.username)
        self.form_class = self.setForm(user)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Config account',
                'form': self.form_class,
            }
        )

    def post(self, request, user):
        userInstance = Users.objects.get(username = user)
        employeInstance = Employes.objects.get(user__username = user)
        employeForm = ConfigEmployeFormClass(request.POST or None, instance = employeInstance)
        passwordForm = ConfigPasswordFormClass(request.POST or None, instance = userInstance)
        userForm = ConfigUserFormClass(
            request.POST or None,
            files = request.FILES,
            instance = userInstance
        )
        #Employe form
        if (
            (request.POST.get('name').upper() != request.user.employes.name or
            request.POST.get('first_lastname').upper() != request.user.employes.first_lastname or
            request.POST.get('second_lastname').upper() != request.user.employes.second_lastname)
            and employeForm.is_valid()
        ):
            try:
                employeForm.save()
                messages.success(request, 'The data user has save successfully.')
            except:
                messages.error(request, 'An error was ocurred while try save user data.')
        #User form
        if (
            (request.POST.get('telephone_number') != request.user.telephone_number or
            request.POST.get('extension') != request.user.extension or
            request.POST.get('email') != request.user.email or
            userForm['profile_image_name'].value()) and
            userForm.is_valid()
        ):
            try:
                preSave = userForm.save(commit = False)
                preSave.password = request.user.password
                if userForm.cleaned_data.get('profile_image_name'):
                    preSave.profile_image = userForm.cleaned_data['profile_image_name'].file.read()
                    preSave.profile_image_name = userForm['profile_image_name'].value()
                preSave.save()
                messages.success(request, 'The user data was saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while trying change user data.')
        #password form
        if (
            (request.POST.get('password') and
            request.POST.get('new_password') and request.POST.get('confirm_new_password')) and
            passwordForm.is_valid()
        ):
            isCorrectPassword = check_password(
                password = passwordForm.cleaned_data.get('password'),
                encoded = request.user.password
            )
            if isCorrectPassword :
                if (
                    passwordForm.cleaned_data.get('new_password') ==
                    passwordForm.cleaned_data.get('confirm_new_password')
                ):
                    try:
                        preSave = passwordForm.save(commit = False)
                        preSave.password = make_password(passwordForm.cleaned_data.get('new_password'))
                        preSave.save()
                        messages.success(request, 'The password was save successfully.')
                    except:
                        messages.error(request, 'An error was ocurred while trying change password')
                else:
                    messages.error(request, 'The new password does not match the confirmation.')
            else:
                messages.error(request, 'Invalid current password.')
        return redirect('configAccountUrl', request.user.username)

    def setForm(self, user):
        instance = Users.objects.prefetch_related('employes').get(username = user)
        forms = {}
        forms['userForm'] = ConfigUserFormClass(
            initial = {
                'telephone_number': instance.telephone_number,
                'extension': instance.extension,
                'email': instance.email
            }
        )
        forms['employeForm'] = ConfigEmployeFormClass(
            initial = {
                'name': instance.employes.name.title(),
                'first_lastname': instance.employes.first_lastname.title(),
                'second_lastname': instance.employes.second_lastname.title(),
            }
        )
        forms['passwordForm'] = ConfigPasswordFormClass
        return forms
