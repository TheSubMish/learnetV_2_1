from django.contrib import admin
from .models import CustomUser,MailToken

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','is_staff']
admin.site.register(CustomUser,CustomUserAdmin)


class ModelTokenAdmin(admin.ModelAdmin):
    list_display = ['user','token']
admin.site.register(MailToken,ModelTokenAdmin)