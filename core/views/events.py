from rest_framework import viewsets

from core.views import UpdateCategoryMixin


class EventsViewSet(UpdateCategoryMixin,
                    viewsets.ViewSet):

    def _update_events(self):
        """
        Update categories based upon given tags
        :return:
        """
        pass

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass
