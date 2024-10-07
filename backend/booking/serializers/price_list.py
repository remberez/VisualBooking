from rest_framework import serializers
from booking.models.price_list import IndependentPriceList


class CurrentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndependentPriceList
        fields = (
            'first_day',
            'last_day',
            'price',
        )
