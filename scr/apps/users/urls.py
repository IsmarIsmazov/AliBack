from django.urls import path

from .views import register_view, login_view, profile_user_view

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('profile_user/', profile_user_view),
]
