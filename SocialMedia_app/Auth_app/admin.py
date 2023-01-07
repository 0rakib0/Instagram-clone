from django.contrib import admin
from .models import CustomUser, User_More_info, Follow
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(User_More_info)
admin.site.register(Follow)