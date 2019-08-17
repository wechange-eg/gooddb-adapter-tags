from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers.events import EventSerializer
from core.serializers.places import PlaceSerializer
from core.views import UpdateCategoryMixin, ValidationMixin


class EventAPIView(UpdateCategoryMixin,
                   ValidationMixin,
                   APIView):

    serializer_class = EventSerializer
    items_key = 'events'
    http_method_names = ['post', 'head', 'options', 'trace']

    def post(self, request):
        """
        Validate items given and update categories
        :return:
        """
        # Validate
        errors = self._validate()
        if errors:
            return Response({'errors': errors}, status=400)
        items = self._update_items(request.data.get(self.items_key))

        return Response({self.items_key: items})


class PlaceAPIView(UpdateCategoryMixin,
                   ValidationMixin,
                   APIView):

    serializer_class = PlaceSerializer
    items_key = 'places'
    http_method_names = ['post', 'head', 'options', 'trace']

    def post(self, request):
        """
        Validate items given and update categories
        :return:
        """
        # Validate
        errors = self._validate()
        if errors:
            return Response({'errors': errors}, status=400)
        items = self._update_items(request.data.get(self.items_key))

        return Response({self.items_key: items})
