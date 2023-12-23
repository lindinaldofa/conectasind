from django.urls import path
from .views import LoginView, register_user, Index
from django.contrib.auth import views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    #path('registrar/', register_user, name='register'),
    path("sair/", views.LogoutView.as_view(), name="logout"),
    path('mudar-senha/', views.PasswordChangeView.as_view(template_name='accounts/atualizar-senha.html'), name="password_change"),
    path('mudar-senha/feito/', views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('recuperar-senha/', views.PasswordResetView.as_view(template_name='accounts/recuperar-senha.html', html_email_template_name='accounts/password_reset_email.html'), name="password_reset"),
    path('recuperar-senha/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='accounts/recuperar-confirma.html'), name="password_reset_confirm"),
    path('recuperar-senha/feito/', views.PasswordResetDoneView.as_view(template_name='accounts/recuperar-enviado.html'), name="password_reset_done"),
    path('recuperar-senha/completo/', views.PasswordResetCompleteView.as_view(template_name='accounts/recuperar-completo.html'), name="password_reset_complete"),
]