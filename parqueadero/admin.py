from django.contrib import admin
from .models import usuario

class UserFields(admin.ModelAdmin):
    list_display = ('email', 'password', 'status')
# Register your models here.
admin.site.register(usuario, UserFields)