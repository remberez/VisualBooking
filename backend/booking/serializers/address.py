from rest_framework import serializers
from booking.models.address import ExactAddress, Address


class ExactAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExactAddress
        fields = (
            'entrance',
            'apartment',
            'floor',
        )


class AddressCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'city',
            'street',
            'house',
            'longitude',
            'latitude',
        )

    def create(self, validated_data):
        return Address.objects.create(
            **validated_data,
            sea_distance=1
        )


class AddressObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'city',
            'street',
            'house',
            'sea_distance',
        )
