from .views import CategoriesClassView, EditCategoryClassView, DeleteCategoryClassView
from django.urls import path



urlpatterns = [
    path('categories/categories/', CategoriesClassView.as_view(), name = 'categoriesUrl'),
    path(
        'categories/edit_category/<slug:slugCategory>',
        EditCategoryClassView.as_view(),
        name = 'editCategoryUrl'
    ),
    path(
        'categories/delete_category/<slug:slugCategory>',
        DeleteCategoryClassView.as_view(),
        name = 'deleteCategoryUrl'
    )
]
