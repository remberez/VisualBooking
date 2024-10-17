import pdb

from django.db.models import Max
from rest_framework import serializers
from booking.models.media import ObjectImage, ObjectVideo


class BaseMediaMixin:

    def create(self, validated_data):
        object_instance = self.context.get('object_instance')
        instances = []
        max_order = self.Meta.model.objects.filter(
            object=object_instance
        ).aggregate(
            max_order=Max('order')
        )['max_order'] or 0

        for media in validated_data['media']:
            media_instance = self.Meta.model.objects.create(
                media=media,
                object=object_instance,
                order=max_order + 1,
            )
            instances.append(media_instance)
            max_order += 1

        return instances


class ObjectImageSerializer(BaseMediaMixin, serializers.ModelSerializer):
    media = serializers.ListField(child=serializers.ImageField())

    class Meta:
        fields = (
            'media',
        )
        model = ObjectImage


class ObjectVideoSerializer(BaseMediaMixin, serializers.ModelSerializer):
    media = serializers.ListSerializer(child=serializers.URLField())

    class Meta:
        fields = (
            'media',
        )
        model = ObjectVideo


class VideoObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectVideo
        fields = (
            'media',
        )


class ImageObjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectImage
        fields = (
            'media',
        )
