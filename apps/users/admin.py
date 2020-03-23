from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.users.models import Users, Group, UserVerifications

User = get_user_model()

admin.site.register(Users)
admin.site.register(Group)
admin.site.register(UserVerifications)
