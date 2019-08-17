from rest_framework import serializers


class CoordinatesSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(required=False)
    zip = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    country = serializers.CharField(required=False)


class ContactSerializer(serializers.Serializer):
    email = serializers.ListField(child=serializers.EmailField())
    phone = serializers.ListField(child=serializers.CharField(), required=False)
    website = serializers.ListField(child=serializers.URLField(), required=False)
