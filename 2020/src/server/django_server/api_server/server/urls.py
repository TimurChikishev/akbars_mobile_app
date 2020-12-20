from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from server.views import RegisterView, UserCreateView, UserListView, UserDetailView
from .models import Profile

urlpatterns = [
   path('user/register/', RegisterView.as_view()),
   path('user/create/', UserCreateView.as_view()),
   path('user/all/', UserListView.as_view()),
   path('user/detail/<int:pk>/', UserDetailView.as_view())

]
