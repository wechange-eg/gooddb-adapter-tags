from rest_framework import serializers

from core.serializers import CoordinatesSerializer, AddressSerializer, ContactSerializer


class EventSerializer(serializers.Serializer):
    REGISTRATION_EMAIL = 'email'
    REGISTRATION_TELEPHONE = 'telephone'
    REGISTRATION_HOMEPAGE = 'homepage'
    REGISTRATION_CHOICES = (REGISTRATION_EMAIL, REGISTRATION_TELEPHONE, REGISTRATION_HOMEPAGE)

    id = serializers.URLField()
    title = serializers.CharField()
    description = serializers.CharField()
    start = serializers.IntegerField()
    end = serializers.IntegerField()
    allDayEvent = serializers.BooleanField()
    createdAt = serializers.IntegerField()
    createdBy = serializers.EmailField()
    coordinates = CoordinatesSerializer()
    address = AddressSerializer()
    contact = ContactSerializer()
    tags = serializers.ListField()
    registration = serializers.ChoiceField(choices=REGISTRATION_CHOICES)
    organizer = serializers.CharField()
