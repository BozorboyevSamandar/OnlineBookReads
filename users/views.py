from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm


# Create your views here.

class Register(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            # create user account
            create_form.save()
            return redirect("users:login")
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        context = {
            'form': login_form
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            # log in the user
            user = login_form.get_user()
            login(request, user)

            return redirect('landing_page')
        else:
            context = {
                'form': login_form
            }
        return render(request, "users/login.html", context)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, 'users/profile.html', {'user': request.user})
