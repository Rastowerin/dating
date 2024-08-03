from django.contrib import admin

from tg_users.models import TgUser


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TgUser._meta.fields]
