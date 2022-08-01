from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'category', 'amount', 'subcategory')

    def create(self, validated_data):
        item = Item(**validated_data)
        item.save()
        return item
