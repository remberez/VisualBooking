from booking.models.address import City
from rest_framework import serializers


class CityListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class CityCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'name',
        )

    def validate(self, attrs):
        attrs['name'] = attrs['name'].capitalize()
        return attrs
