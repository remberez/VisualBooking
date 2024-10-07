from django.db.models import Min
from rest_framework import serializers
from booking.models.object import Object, IndependentObject, Room
from common.mixins.serializer_mixins import CommonMixin
from booking.models.address import Address, ExactAddress
from booking.models.price_list import IndependentPriceList
from rest_framework import exceptions
from booking.serializers.address import AddressCreateSerializer, ExactAddressCreateSerializer, \
    AddressObjectListSerializer


class IndependentObjectCreateSerializer(serializers.ModelSerializer):
    exact_address = ExactAddressCreateSerializer(required=False)

    class Meta:
        model = IndependentObject
        fields = (
            'rooms',
            'square',
            'adult',
            'kid',
            'sleeping_places',
            'exact_address',
        )


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'rooms',
            'square',
            'adult',
            'kid',
            'sleeping_places',
        )


class ObjectValidate(CommonMixin):
    def validate(self, attrs):
        attrs = self.to_capitalize(attrs, ['name', 'description'])
        return attrs


class ObjectCreateSerializer(ObjectValidate, serializers.ModelSerializer):
    object_instance: Object
    address = AddressCreateSerializer()
    independent_object = IndependentObjectCreateSerializer(required=False)
    rooms = RoomCreateSerializer(many=True, required=False)

    class Meta:
        model = Object
        fields = (
            'name',
            'description',
            'number_of_flat',
            'address',
            'type',
            'independent_object',
            'rooms',
        )
        
    def validate(self, attrs):
        if attrs['type'].is_independent and not attrs.get('independent_object', None):
            raise exceptions.ParseError('Отсутствуют поля independent_object, exact_address')
        if not attrs['type'].is_independent and not attrs.get('rooms', None):
            raise exceptions.ParseError('Отсутствуют поля rooms')
        return super().validate(attrs)

    def create_object(self, **object_data):
        return self.Meta.model.objects.create(
            **object_data
        )

    def create_independent_object(self, independent_object_data):
        if self.object_instance and self.object_instance.type.is_independent:
            exact_address_instance = ExactAddress.objects.create(
                **independent_object_data.pop('exact_address'),
            )
            IndependentObject.objects.create(
                exact_address=exact_address_instance,
                base_object=self.object_instance,
                **independent_object_data,
            )

    def create_rooms(self, rooms_data):
        if self.object_instance and not self.object_instance.type.is_independent:
            if self.object_instance:
                for room in rooms_data:
                    Room.objects.create(
                        **room,
                        base_object=self.object_instance,
                    )

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        independent_object_data = validated_data.pop('independent_object', None)
        rooms_data = validated_data.pop('rooms', None)

        address_instance = Address.objects.create(**address_data, sea_distance=1)
        object_instance = self.create_object(
            address=address_instance,
            owner=self.context.get('request').user,
            **validated_data
        )
        self.object_instance = object_instance
        self.create_independent_object(independent_object_data)
        self.create_rooms(rooms_data)
        return object_instance


class ObjectListSerializer(serializers.ModelSerializer):
    address = AddressObjectListSerializer()
    currently_price = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'name',
            'address',
            'currently_price',
        )
        model = Object

    def get_currently_price(self, obj) -> float:
        # request = self.context.get('request')
        # first_day = request.query_params.get('first_day')
        # last_day = request.query_params.get('last_day')
        #
        # if first_day and last_day:
        #     try:
        #         min_price = IndependentPriceList.objects.filter(
        #             object=obj,
        #             first_day__gte=IndependentPriceList.objects.filter(
        #                 object=obj,
        #                 first_day__lte=first_day
        #             ).order_by(
        #                 '-first_day'
        #             ).first().first_day,
        #
        #             last_day__lte=IndependentPriceList.objects.filter(
        #                 object=obj,
        #                 last_day__gte=last_day
        #             ).order_by(
        #                 'last_day'
        #             ).first().last_day,
        #         ).order_by('price').values('price').first()
        #
        #     except AttributeError:
        #         raise exceptions.ParseError('Ошибка')
        #     return min_price
        # return IndependentPriceList.objects.filter(
        #     object=obj
        # ).aggregate(
        #     min_price=Min('price')
        # )['min_price']
        return 1.0
