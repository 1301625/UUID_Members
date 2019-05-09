
# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.translation import ugettext_lazy as _

class ProfileInline(admin.TabularInline):
    model = Profile



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uuid','email' ,'nick_name','is_staff']
    search_fields = ('email','nick_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('nick_name',)}),
        (_('허가'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    inlines = [ProfileInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass