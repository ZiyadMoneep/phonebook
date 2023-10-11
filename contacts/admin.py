from django.contrib import admin
from .models import Contact, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PhoneNumberInline]


admin.site.register(Contact, ContactAdmin)
