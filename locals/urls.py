from .views import LocalsClassView, EditLocalClassView, DeleteLocalsClassView
from django.urls import path



urlpatterns = [
    path('locals/all_locals/', LocalsClassView.as_view(), name = 'localsUrl'),
    path(
        'locals/edit_local/<slug:slugLocal>',
        EditLocalClassView.as_view(),
        name = 'editLocalUrl'
    ),
    path(
        'locals/delete_local/<slug:slugLocal>',
        DeleteLocalsClassView.as_view(),
        name = 'deleteLocalUrl'
    )
]
