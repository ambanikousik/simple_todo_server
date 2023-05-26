from django.urls import path

from .views import RegisterView, LoginView, UserDataView

urlpatterns = [
    path("user/", UserDataView.as_view(), name="user-data"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
