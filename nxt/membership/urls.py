from django.contrib import admin
from django.urls import include, path
from .views import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile')
]
