from django import forms
from django.core.mail import send_mail

from users.models import CustomUser


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class UserUpdateProfile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_pic')


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=15)

# class UserCreateForm(forms.Form):
#     username = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     password = forms.CharField(max_length=18)
#
#     def save(self):
#         username = self.cleaned_data['username']
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         user = User.objects.create(
#             username=username,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#         )
#         user.set_password(password)
#         user.save()
#
#         return user
