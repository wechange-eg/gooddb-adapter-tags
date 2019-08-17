from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    url = serializers.URLField()
    primary = serializers.BooleanField()
    title = serializers.CharField()


class OpeningHoursSerializer(serializers.Serializer):
    description = serializers.CharField()
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
    description = serializers.CharField()
    placeType = serializers.ChoiceField(choices=PLACETYPE_CHOICES)
    images = ImageSerializer(many=True)
    coordinates = CoordinatesSerializer()
    address = AddressSerializer()
    contact = ContactSerializer()
    categories = serializers.ListField()
    tags = serializers.ListField()
    rating = serializers.FloatField()
    openingHours = OpeningHoursSerializer()
    license = serializers.CharField()
    priceLevel = serializers.ChoiceField(choices=PRICELEVEL_CHOICES)
    source = serializers.CharField()
    additionalProperties = serializers.ListField()
