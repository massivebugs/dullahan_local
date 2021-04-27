from django.urls import path
from .views import home_view, about_view, log_in, log_out, sign_up


urlpatterns = [
    path('', home_view, name='get_home'),
    path('about/', about_view, name='get_about'),
    path('accounts/login/', log_in, name='log_in'),
    path('accounts/logout/', log_out, name='log_out'),
    path('accounts/signup/', sign_up, name='sign_up'),
]
