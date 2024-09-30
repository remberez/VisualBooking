from django.contrib import admin
from booking.models.address import Address
from booking.models.object import Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_active')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house')
