import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Profile, Chat, Party, Messages

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

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    logger.info(serializers.CurrentUserDefault)
    class Meta:
        model = User
        fields = ("id","username","first_name","last_name","email", "profile")
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email")


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('contect',)

# Отправляется сообщение
# Если для пользователя был создан чат, то добавляем сообщение, иначе
# создаем чат для пользователя и добавляем сообщение
# ***TO-DO***
# Если из-за слабого интернета сообщение не дошло
# Нужно резервировать его порядковый id, чтобы
# сообщения имели правильный порядок отправки, 
# чтобы избежать недопониманий между собеседниками
# ***
class ChatSerializer(serializers.ModelSerializer):
    massege = MessagesSerializer()
    class Meta:
        model = Chat
        fields = ("massege",)
            
    def create(self, request):
        user_id = self.context['request'].user.id
        
        if not Chat.objects.filter(user_id=user_id).exists():
            chat = Chat.objects.create(
                user_id = user_id,
            )
   
        massege_data = request.pop('massege')
        chat = Chat.objects.filter(user_id=user_id).first()
        chat_id = chat.chat_id
        message_id = self.get_masseg_id(chat_id)
       
        message = Messages.objects.create(
            message_id = message_id,
            chat_id = chat_id,
            user_id = user_id,
            contect = massege_data['contect'],
            # etc...
        )

        return chat

    def get_masseg_id(self, chat_id):
        if Messages.objects.filter(chat_id=chat_id).last(): 
            last_massage = Messages.objects.filter(chat_id=chat_id).last()
            next_id = last_massage.message_id + 1
            return next_id
        else:
            return 1

    def _user_id(self, obj):
        request = self.context.get('request', None)
        if request:
            logger.info('User ID REQUEST: {}'.format(request.user.id))
            return request.user.id