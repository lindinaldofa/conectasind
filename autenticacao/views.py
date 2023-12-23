from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuário criado - <a href="/login">Entre na sua conta</a>.'
            success = True

            if user is not None:
                login(request, user)
                return redirect("/app")
        else:
            msg = 'As informações não foram validadas'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

class Index(LoginRequiredMixin, TemplateView):
    login_url="/login/"
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
