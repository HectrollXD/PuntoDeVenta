from .forms import AddNewCategoryFormClass, SearchCategoriesFormClass
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins import GroupRequiredMixin
from django.contrib import messages
from .models import Categories
from django.views import View
from app import getAppName



#--------------------------------------------------------------------------------------------------- Providers view
class CategoriesClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]
    template_name = 'category.html'
    queryset = None
    form_class = {
        'searchForm': SearchCategoriesFormClass,
        'addForm': AddNewCategoryFormClass,
    }
    
    def get(self, request):
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Categories',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )
    
    def post(self, request):
        form = self.form_class['addForm'](request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The category has been saved successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to save new category.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('categoriesUrl')



#--------------------------------------------------------------------------------------------------- Edit Provider
class EditCategoryClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]
    template_name = 'category.html'
    queryset = None
    form_class = {
        'searchForm': SearchCategoriesFormClass,
    }

    def get(self, request, slugCategory):
        category = get_object_or_404(Categories, category_alias = slugCategory)
        self.form_class['addForm'] = AddNewCategoryFormClass(instance = category)
        self.queryset = setQuery(request)
        return render(
            request,
            template_name = self.template_name,
            context = {
                'appName': getAppName(),
                'titleOfPage': 'Categories',
                'queryset': self.queryset,
                'form': self.form_class,
            }
        )

    def post(self, request, slugCategory):
        category = get_object_or_404(Categories, category_alias = slugCategory)
        form = AddNewCategoryFormClass(request.POST or None, instance = category)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'The category has been updated successfully.')
            except:
                messages.error(request, 'An error was ocurred while try to update category.')
        else:
            messages.error(request, 'Check that the fields are written correctly.')
        return redirect('categoriesUrl')



#--------------------------------------------------------------------------------------------------- Delete providers
class DeleteCategoryClassView( LoginRequiredMixin, GroupRequiredMixin, View ):
    login_url = 'loginUrl'
    group_required = [1, 2]

    def get(self, request, slugCategory):
        category = get_object_or_404(Categories, category_alias = slugCategory)
        try:
            category.delete()
            messages.success(request, 'The category was deleted successfully.')
        except:
            messages.error(request, 'An error was occured while try to delete the category.')
        return redirect('categoriesUrl')



#--------------------------------------------------------------------------------------------------- Fucntion to set queryset
def setQuery(request):
    query = Categories.objects.all()
    searches = getSearch(request)
    if searches['category_name']:
        query = query.filter(category_name__icontains = searches['category_name'])
    query = query.order_by('category_name')
    return query



#--------------------------------------------------------------------------------------------------- Fucntion to get searches
def getSearch(request):
    searches = {
        'category_name': request.GET.get('category_name'),
    }
    return searches