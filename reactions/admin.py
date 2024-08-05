from django.contrib import admin

from reactions.models import Reaction


@admin.register(Reaction)
class TgUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reaction._meta.fields]
