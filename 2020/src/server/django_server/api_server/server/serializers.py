import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Profile, Chat, Party, Messages, VirtualAccount

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

class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"
        lookup_field = "chat_id"

class CreateVirtualAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAccount
        fields = ("name", "primary_contact", "email_id", "mobile_number", 
                    "created_at", "updated_at")

        # to do
        # дописать генирацию 
        # virtual_account_number
        # virtual_account_ifsc_code
        # vpa
        def create(self, validated_data):
            try:
                last_virtual_account = VirtualAccount.objects.latest("created_at")
            except VirtualAccount.DoesNotExist:
                last_virtual_account = None

            logger.info("last_virtual_account:")
            logger.info(last_virtual_account)

            if (last_virtual_account == None): virtual_account_number = "100000000000000"
            else: logger.info(virtual_account_number)  

            va_ifsc_code = "ICIC#" # to do (генерация)
            va_vpa = "open.#@icici" # to do (генерация)
            data = validated_data.pop('virtualaccount')
            
            virtualaccount = VirtualAccount.objects.create(
                virtual_account_number = last_virtual_account,
                virtual_account_ifsc_code = va_ifsc_code,
                vpa = va_vpa,
                name = data['name'],
                primary_contact = data['primary_contact'],
                contact_type = data['contact_type'],
                email_id = data['email_id'],
                mobile_number = data['mobile_number'],
            )
            logger.info("virtualaccount:")
            logger.info(virtualaccount)
            return virtualaccount

class VirtualAccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAccount
        fields = "__all__"