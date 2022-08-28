from django.urls import path
from .views import UsersDetailApiView, UsersListApiView

urlpatterns = [
    path("users/", UsersListApiView.as_view()),
    path("users/<int:user_id>/", UsersDetailApiView.as_view()),
]
