from . import views, models
from django.urls import path


urlpatterns = [

    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.NewLoginView.as_view(), name="login"),
    path("user/", views.ListView.as_view(), name="user"),
]