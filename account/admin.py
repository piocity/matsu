from django.contrib import admin

from account.models import UserProfile

# Register your models here.

'''class UserProfileAdmin(admin.ModelAdmin):
    fields = ['username',]
    list_display = ['username',]
    list_filter = ['username',]
    search_fields = ['username',]

admin.site.register(UserProfile, UserProfileAdmin)
'''
