from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from core.views.events import EventAPIView, PlaceAPIView

schema_view = get_swagger_view(title='GoodDB Adapter Tags API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/events$', EventAPIView.as_view()),
    url(r'^api/v1/places$', PlaceAPIView.as_view()),
    url(r'^api/v1/docs$', schema_view),
]

# Non i18n patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
