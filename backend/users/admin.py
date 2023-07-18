from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('username', 'email',)
    search_fields = ('username', 'email', 'first_name', 'last_name')


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'user',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.unregister(Group)
