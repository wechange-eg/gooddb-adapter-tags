from rest_framework import serializers

from core.serializers import CoordinatesSerializer, AddressSerializer, ContactSerializer


class EventSerializer(serializers.Serializer):
    REGISTRATION_EMAIL = 'email'
    REGISTRATION_TELEPHONE = 'telephone'
    REGISTRATION_HOMEPAGE = 'homepage'
    REGISTRATION_CHOICES = (REGISTRATION_EMAIL, REGISTRATION_TELEPHONE, REGISTRATION_HOMEPAGE)

    id = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    start = serializers.IntegerField()
    end = serializers.IntegerField(required=False)
    allDayEvent = serializers.BooleanField(required=False)
    createdAt = serializers.IntegerField()
    coordinates = CoordinatesSerializer()
    address = AddressSerializer(required=False)
    contact = ContactSerializer()
    tags = serializers.ListField(required=False)
    registration = serializers.ChoiceField(choices=REGISTRATION_CHOICES, required=False)
    organizer = serializers.CharField(required=False)
