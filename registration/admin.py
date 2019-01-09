from django.contrib import admin
from .models import Profile

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('user','avatar','bio','link')

admin.site.register(Profile, RegisterAdmin)

