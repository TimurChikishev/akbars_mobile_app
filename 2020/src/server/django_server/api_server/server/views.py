from django.shortcuts import render
from rest_framework import generics, permissions
from server.serializers import *
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class RegisterView(generics.GenericAPIView):
    global logger
    serializer_class = UserProfileSerializer
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        logger.info("serializer: {}".format(serializer))
        logger.info("serializer.is_valid(): {}".format(serializer.is_valid()))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'OK'}, status=status.HTTP_201_CREATED)
  
        custom_error_messages = []
        
        if 'username' in serializer.errors:
            custom_error_messages.append({'_message':"Username is already in use."})
        if 'email' in serializer.errors:
            custom_error_messages.append({'_message':"Email is already in use."})
        if 'profile' in serializer.errors:
            custom_error_messages.append({'_message':"Passport is already in use."})
    
        return Response(custom_error_messages, status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserDetailSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    logger.debug('Enter To UserDetailView')
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    




