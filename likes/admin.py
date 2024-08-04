from django.contrib import admin

from likes.models import Like


@admin.register(Like)
class TgUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields]
