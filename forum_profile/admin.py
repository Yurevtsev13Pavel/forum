from profile import Profile

from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    exclude = ['id']
    search_fields = ['username', 'description', 'signature', 'profile_color']
    list_display = ['username', 'photo', 'profile', 'user']
    list_editable = ['photo', 'color']
