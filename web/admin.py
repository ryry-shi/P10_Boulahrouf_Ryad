from django.contrib import admin
from .models import User, Projects, Contributors

class UserAdmin(admin.ModelAdmin):
    
    list_display = ("first_name", "password")

class ProjectAdmin(admin.ModelAdmin):

    list_display = ("title", "description")

admin.site.register(User)
admin.site.register(Projects)
admin.site.register(Contributors)
# Register your models here.
