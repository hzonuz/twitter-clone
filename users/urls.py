from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from users.views import RegisterUserView, LogoutView, UserDetailView

app_name = "users"
urlpatterns = [
    path("signup/", RegisterUserView.as_view(), name="signup"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("<user_pk>/", UserDetailView.as_view(), name="user-detail")
]
