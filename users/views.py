from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm


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

            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password)
            user.save()

            return redirect("users:login")
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")
