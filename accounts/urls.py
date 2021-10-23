from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('' ,  views.home , name="home"),
    path('login/', views.login_page, name='login_page'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('authenticated/', views.account_authenticated, name='account_authenticated'),
    

]