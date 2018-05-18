from django.urls import path
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )

app_name = 'contas'
urlpatterns = [

    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'contas/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'contas/logout.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.view_perfil, name='view_perfil'),
    path('perfil/edit/', views.edit_perfil, name='edit_perfil'),
    path('trocar-password/', views.trocar_password, name='trocar_password'),
    path('reset-password/', PasswordResetView.as_view(), {'template_name': 'contas/reset_password.html', 'post_reset_redirect': 'contas:password_reset_done'},
    name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
    PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
