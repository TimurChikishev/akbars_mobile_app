from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

# Модель расширения дефолтного класса User
# to do:
# mobile_number
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", unique=True, on_delete=models.CASCADE)
    passport = models.CharField(unique=True, max_length=11) 

# Таблица со списком чатов
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True, null=False) # id чата
    user_id = models.IntegerField(null=False) # Создатель чата

# Таблица со списком участников
class Party(models.Model):
    chat_id = models.IntegerField(null=False) # id чата 
    user_id = models.IntegerField(null=False) # id участника

# Таблица со списком сообщений
class Messages(models.Model):
    message_id = models.IntegerField(null=False) # порядковый id сообщения в чате 
    chat_id = models.IntegerField(null=False) # id чата 
    user_id = models.IntegerField(null=False) # id участника, который добавил сообщение
    contect = models.CharField(max_length=4096, null=False) # текст сообщения
    created = models.DateTimeField(auto_now_add=True, null=False) # дата и время создания
    is_read = models.BooleanField(default=False, null=False) # прочитано ли сообщение

class VirtualAccount(models.Model): # id - virtual_account_id
    virtual_account_number = models.CharField(max_length=255, null=False) # № счёта
    virtual_account_ifsc_code = models.CharField(max_length=255, null=False) # ifsc
    vpa = models.CharField(max_length=255, null=False) # UPI ID
    name = models.CharField(max_length=255, null=False) # название компании клиента (если физ. лицо имя клиента)
    primary_contact = models.CharField(max_length=255, null=False) # Имя заказчика
    contact_type = models.CharField(max_length=255, null=False) # Тип контакта 
    email_id = models.CharField(max_length=255, null=False) # email id клиента
    landline_number = models.IntegerField(null=True) # номер наземной линии связи
    mobile_number = models.CharField(max_length=10, null=False) # номер мобильника
    created_at = models.DateTimeField(auto_now_add=True, null=False) # дата и время создания
    updated_at = models.DateTimeField(auto_now=True, null=False) # дата и время update