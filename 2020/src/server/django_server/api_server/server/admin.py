from django.contrib import admin
from .models import Profile, Party, Chat, Messages, VirtualAccount
# Register your models here.

admin.site.register(Profile)
admin.site.register(Chat)
admin.site.register(Messages)
admin.site.register(Party)
admin.site.register(VirtualAccount)