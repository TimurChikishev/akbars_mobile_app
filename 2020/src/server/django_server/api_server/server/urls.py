from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from server.views import (RegisterView, UserCreateView, 
UserListView, UserDetailView, MessageView, MessageListView)


urlpatterns = [
   path('send/message/', MessageView.as_view()),
   path('user/register/', RegisterView.as_view()),
   path('user/create/', UserCreateView.as_view()),
   path('user/all/', UserListView.as_view()),
   path('user/detail/<int:pk>/', UserDetailView.as_view()),
   path('get/message/<int:chat_id>/', MessageListView.as_view()),
]
