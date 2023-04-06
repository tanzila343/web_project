from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Backend_Management_App.models import Beds, Rooms, CustomUser


admin.site.register(Beds)
admin.site.register(Rooms)

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)

