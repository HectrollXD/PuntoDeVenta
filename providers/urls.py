from .views import ProvidersClassView, EditProviderClassView, DeleteProviderClassView
from django.urls import path



urlpatterns = [
    path('providers/providers/', ProvidersClassView.as_view(), name = 'providersUrl'),
    path(
        'providers/edit_provider/<slug:slugProvider>',
        EditProviderClassView.as_view(),
        name = 'editProviderUrl'
    ),
    path(
        'providers/delete_provider/<slug:slugProvider>',
        DeleteProviderClassView.as_view(),
        name = 'deleteProviderUrl'
    )
]
