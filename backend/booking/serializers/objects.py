from rest_framework import serializers
from booking.models.object import Object
from common.mixins.serializer_mixins import CommonMixin
from booking.models.address import Address


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'city',
            'street',
            'house',
            'entrance',
            'apartment',
            'longitude',
            'latitude',
        )


class ObjectInfoSerializer(serializers.Serializer):
    number_of_room = serializers.IntegerField()
    number_of_floors = serializers.IntegerField()
    square = serializers.IntegerField()
    floor = serializers.IntegerField()


class ObjectValidate(CommonMixin):
    def validate(self, attrs):
        attrs = self.to_capitalize(attrs, ['name', 'description'])
        return attrs


class ObjectCreateSerializer(ObjectValidate, serializers.ModelSerializer):
    address = AddressCreateSerializer()
    info_about_object = ObjectInfoSerializer()

    class Meta:
        model = Object
        fields = (
            'name',
            'description',
            'adult',
            'kid',
            'sea_distance',
            'info_about_object',
            'address',
        )

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        info_about_object_data = validated_data.pop('info_about_object')

        address_serializer = AddressCreateSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_instance = address_serializer.save()

        validated_data = {**validated_data, **info_about_object_data}
        object_instance = self.Meta.model.objects.create(
            address=address_instance,
            owner=self.context.get('request').user,
            **validated_data
        )

        validated_data['address'] = address_serializer.data
        self._data = validated_data
        return object_instance
