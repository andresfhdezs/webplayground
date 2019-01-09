from django.urls import path
from .views import ProfileList, ProfileDetailView

profiles_patterns = ([
    path('', ProfileList.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], "profiles")