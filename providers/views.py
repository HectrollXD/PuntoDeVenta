from .forms import AddNewProviderFormClass, SearchProvidersFormClass
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from mixins import GroupRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Providers
from app import getAppName



#--------------------------------------------------------------------------------------------------- Providers view
class ProvidersClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]
    template_name = 'providers.html'
    queryset = None
    form_class = {
        'searchForm': SearchProvidersFormClass,
        'addForm': AddNewProviderFormClass,
    }
    
    def get(self, request):
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Providers',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )
    
    def post(self, request):
        form = self.form_class['addForm'](request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The provider has been saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to save new provider.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('providersUrl')



#--------------------------------------------------------------------------------------------------- Edit Provider
class EditProviderClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]
    template_name = 'providers.html'
    queryset = None
    form_class = {
        'searchForm': SearchProvidersFormClass,
    }

    def get(self, request, slugProvider):
        provider = get_object_or_404(Providers, provider_alias = slugProvider)
        self.form_class['addForm'] = AddNewProviderFormClass(instance = provider)
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Providers',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def post(self, request, slugProvider):
        provider = get_object_or_404(Providers, provider_alias = slugProvider)
        form = AddNewProviderFormClass(request.POST or None, instance = provider)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The provider has been updated successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to update provider.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('providersUrl')



#--------------------------------------------------------------------------------------------------- Delete providers
class DeleteProviderClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]

    def get(self, request, slugProvider):
        provider = get_object_or_404(Providers, provider_alias = slugProvider)
        try:
            provider.delete()
            messages.success(request, 'The provider was deleted successfully.')
        except:
            messages.error(request, 'An error was occured while try to delete the provider.')
        return redirect('providersUrl')



#--------------------------------------------------------------------------------------------------- Fucntion to set queryset
def setQuery(request):
    query = Providers.objects.all()
    searches = getSearch(request)
    if searches['provider_name']:
        query = query.filter(provider_name__icontains = searches['provider_name'])
    query = query.order_by('provider_name')
    return query



#--------------------------------------------------------------------------------------------------- Fucntion to get searches
def getSearch(request):
    searches = {
        'provider_name': request.GET.get('provider_name'),
    }
    return searches