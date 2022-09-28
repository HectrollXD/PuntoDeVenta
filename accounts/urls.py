from .views import LoginClassView, CreateAcountClassView, LogoutClassView, ConfigureAccountClassView
from .views import ShowAllAccountClassView, EditAccountClassView, DeleteAccountClassVies
from django.urls import path



urlpatterns = [
    path('', LoginClassView.as_view(), name = 'loginUrl'),
    path('logout/', LogoutClassView.as_view(), name = 'logoutUrl'),
    path('accounts/create_account/', CreateAcountClassView.as_view(), name = 'createAccountUrl'),
    path('accounts/all_accounts/', ShowAllAccountClassView.as_view(), name = 'showAllAccountsUrl'),
    path(
        'accounts/config/<str:user>',
        ConfigureAccountClassView.as_view(),
        name = 'configAccountUrl'
    ),
    path(
        'accounts/edit_account/user_<str:user>',
        EditAccountClassView.as_view(),
        name = 'editAccountUrl'
    ),
    path(
        'accounts/delete_accont/<int:userId>',
        DeleteAccountClassVies.as_view(),
        name = 'deleteAccountUrl'
    ),
]