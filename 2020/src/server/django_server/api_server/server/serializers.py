import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Profile

logger = logging.getLogger(__name__)
User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','passport')
        read_only_fields = ('user',)

class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
  
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'profile',)
        # error_messages = {"username": {"Message":"Username is already in use."}, 
        # 'email':{"Message":"Email is already in use."}}

        extra_kwargs = {
                    'password': {
                        'write_only': True,
                    }
                }

    def validate_email(self, attrs):
        logger.info(attrs)
        data = self.get_initial()
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already in use.')
        return super().validate(attrs)


    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
        )

        profile_data = validated_data.pop('profile')
        
        profile = Profile.objects.create(
            user = user,
            passport = profile_data['passport'],
            # etc...
        )

        return user

    # def create(self, validated_data):
    #     logger.info("validated_data", **validated_data)
    #     profile_data = validated_data.pop('profile', None)

    #     user = User.objects.create(**validated_data)

    #     Profile.objects.create(user=user, passport = profile_data['passport'])
    #     return user

       
        # profile = Profile.objects.create(
        #     user=User,
        #     passport = profile_data['passport']
        # )
        # logger.info('Profile.objects.create: {}'.format(profile))
        # return user

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ("id","username","first_name","last_name","email", "profile")

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email")
