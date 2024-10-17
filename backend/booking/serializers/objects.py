from itertools import chain
from rest_framework import serializers
from booking.models.media import ObjectImage, ObjectVideo
from booking.models.object import Object, IndependentObject, Room
from booking.serializers.media import ImageObjectListSerializer, VideoObjectListSerializer
from common.mixins.serializer_mixins import CommonMixin
from booking.models.address import Address, ExactAddress
from rest_framework import exceptions
from booking.serializers.address import AddressCreateSerializer, ExactAddressCreateSerializer, \
    AddressObjectListSerializer
from booking.serializers.tags import TagListSerializer


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
    min_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    images = ImageObjectListSerializer(many=True)
    tags = serializers.SerializerMethodField(method_name='get_tags')
    videos = VideoObjectListSerializer(many=True)

    class Meta:
        fields = (
            'id',
            'name',
            'address',
            'min_price',
            'type',
            'images',
            'videos',
            'tags',
        )
        model = Object

    def get_tags(self, obj):
        tags = []
        data = obj.rooms.all() if not obj.type.is_independent else [obj.independent]
        for i in data:
            tags.append(i.tags.all())
        tags = list(set(chain(*tags)))[:7]
        serializer = TagListSerializer(tags, many=True)
        return serializer.data
