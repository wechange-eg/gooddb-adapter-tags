from rest_framework import serializers


class CoordinatesSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField()
    zip = serializers.CharField()
    city = serializers.CharField()
    country = serializers.CharField()


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    website = serializers.URLField()
