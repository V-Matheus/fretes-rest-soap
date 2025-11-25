from django.urls import path
from .views import FretesView
from .views_docs import DocsView, OpenApiJsonView

urlpatterns = [
    path('fretes', FretesView.as_view(), name='fretes'),
    path('docs/', DocsView.as_view(), name='docs'),
    path('docs/openapi.json', OpenApiJsonView.as_view(), name='openapi'),
]
