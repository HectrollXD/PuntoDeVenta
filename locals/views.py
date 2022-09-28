from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from .forms import AddNewLocalFormClass, SearchLocalFormClass
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins import GroupRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Locals
from app import getAppName



#--------------------------------------------------------------------------------------------------- Add new local
class LocalsClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]
    template_name = 'locals.html'
    queryset = None
    form_class = {
        'searchForm': SearchLocalFormClass,
        'addForm': AddNewLocalFormClass,
    }

    def get(self, request):
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Locals',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def post(self, request):
        form = self.form_class['addForm'](request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The local has been saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to save new local.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('localsUrl')



#--------------------------------------------------------------------------------------------------- Edite Local
class EditLocalClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]
    template_name = 'locals.html'
    queryset = None
    form_class = {
        'searchForm': SearchLocalFormClass,
    }

    def get(self, request, slugLocal):
        local = get_object_or_404(Locals, local_alias = slugLocal)
        self.form_class['addForm'] = AddNewLocalFormClass(instance = local)
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Locals',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def post(self, request, slugLocal):
        local = get_object_or_404(Locals, local_alias = slugLocal)
        form = AddNewLocalFormClass(request.POST or None, instance = local)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The local has been updated successfully.')
            except:
                messages.error('An error was ocurred while try to update local.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('localsUrl')



#--------------------------------------------------------------------------------------------------- Delete Locals
class DeleteLocalsClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1]

    def get(self, request, slugLocal):
        local = get_object_or_404(Locals, local_alias = slugLocal)
        try:
            local.delete()
            messages.success(request, 'The local was deleted successfully.')
        except:
            messages.error(request, 'An error was occured while try to delete the local.')
        return redirect('localsUrl')



#--------------------------------------------------------------------------------------------------- Fucntion to set queryset
def setQuery(request):
    query = Locals.objects.all()
    searches = getSearch(request)
    if searches['local_name']:
        query = query.filter(local_name__icontains = searches['local_name'])
    if searches['city']:
        query = query.filter(city__icontains = searches['city'])
    if searches['state']:
        query = query.filter(state__icontains = searches['state'])
    query = query.order_by('local_name')
    return query



#--------------------------------------------------------------------------------------------------- Fucntion to get searches
def getSearch(request):
    searches = {
        'local_name': request.GET.get('local_name'),
        'city': request.GET.get('city'),
        'state': request.GET.get('state'),
    }
    return searches