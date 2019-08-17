from rest_framework import serializers

from core.serializers import CoordinatesSerializer, AddressSerializer, ContactSerializer


class ImageSerializer(serializers.Serializer):
    url = serializers.URLField()
    primary = serializers.BooleanField(required=False)
    title = serializers.CharField(required=False)


class OpeningHoursSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)
    periods = serializers.ListField()


class PlaceSerializer(serializers.Serializer):
    PLACETYPE_PROJECT = 'Project'
    PLACETYPE_GROUP = 'Group'
    PLACETYPE_FOOD = 'Food'
    PLACETYPE_STORE = 'Store'
    PLACETYPE_ACCOMODATION = 'Accomodation'
    PLACETYPE_PUBLIC_INFRASTRUCTURE = 'Public Infrastructure'
    PLACETYPE_CHOICES = (PLACETYPE_PROJECT, PLACETYPE_GROUP, PLACETYPE_FOOD, PLACETYPE_STORE, PLACETYPE_ACCOMODATION,
                         PLACETYPE_PUBLIC_INFRASTRUCTURE)

    PRICELEVEL_FREE = 0
    PRICELEVEL_INEXPENSIVE = 1
    PRICELEVEL_MODERATE = 2
    PRICELEVEL_EXPENSIVE = 3
    PRICELEVEL_VERY_EXPENSIVE = 4
    PRICELEVEL_CHOICES = (PRICELEVEL_FREE, PRICELEVEL_INEXPENSIVE, PRICELEVEL_MODERATE, PRICELEVEL_EXPENSIVE,
                          PRICELEVEL_VERY_EXPENSIVE)

    id = serializers.URLField()
    version = serializers.IntegerField(read_only=False)
    createdAt = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    placeType = serializers.ChoiceField(choices=PLACETYPE_CHOICES, required=False)
    images = ImageSerializer(many=True, required=False)
    coordinates = CoordinatesSerializer()
    address = AddressSerializer(required=False)
    contact = ContactSerializer()
    categories = serializers.ListField(required=False)
    tags = serializers.ListField(required=False)
    rating = serializers.FloatField(required=False)
    openingHours = OpeningHoursSerializer(required=False)
    license = serializers.CharField(required=False)
    priceLevel = serializers.ChoiceField(choices=PRICELEVEL_CHOICES, required=False)
    source = serializers.CharField()
    additionalProperties = serializers.ListField(required=False)
