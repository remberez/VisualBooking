from rest_framework import serializers
from booking.models.tags import Tag


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'title',
            'svg',
        )
