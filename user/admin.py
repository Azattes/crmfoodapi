from django.contrib import admin
from user.models import User, Role
from firebase import UserService


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        UserService.create(obj.phone)
        super().save_model(request, obj, form, change)


admin.site.register(Role)
