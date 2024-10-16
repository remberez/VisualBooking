from django.contrib import admin
from booking.models.address import Address, ExactAddress, City
from booking.models.object import Object, IndependentObject, Room, TypeOfObject
from booking.models.media import ObjectImage, ObjectVideo
from booking.models.price_list import IndependentPriceList, PriceListOfRoom
from booking.models.tags import Tag


class IndependentObjectInline(admin.TabularInline):
    model = IndependentObject
    extra = 0


class RoomsInline(admin.TabularInline):
    model = Room
    extra = 0


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house')


class ObjectImageAdmin(admin.TabularInline):
    model = ObjectImage
    extra = 0


class ObjectVideoAdmin(admin.TabularInline):
    model = ObjectVideo
    extra = 0


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'is_active')
    inlines = (
        ObjectImageAdmin,
        ObjectVideoAdmin,
        IndependentObjectInline,
        RoomsInline,
    )


@admin.register(IndependentPriceList)
class IndependentPriceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'first_day', 'last_day')


@admin.register(ExactAddress)
class ExactAddressAdmin(admin.ModelAdmin):
    list_display = ('entrance', 'apartment', 'floor')


@admin.register(IndependentObject)
class IndependentObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'base_object', 'created_at', 'updated_at')


@admin.register(Room)
class RoomObject(admin.ModelAdmin):
    list_display = ('id', 'base_object', 'created_at', 'updated_at')


@admin.register(TypeOfObject)
class TypeOfObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_independent')


@admin.register(PriceListOfRoom)
class PriceListOfRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'first_day', 'last_day')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
