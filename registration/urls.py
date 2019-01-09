from django.urls import path
from .views import SignUpView, ProfileView, EmailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/mail', EmailView.as_view(), name='profile_email'),
]