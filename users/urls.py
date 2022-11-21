from django.urls import path
from .views import Register, LoginView, ProfileView

app_name = 'users'
urlpatterns = [
    path('register', Register.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('profile', ProfileView.as_view(), name="profile"),
]
