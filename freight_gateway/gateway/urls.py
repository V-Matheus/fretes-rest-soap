from django.urls import path
from .views import FretesView

urlpatterns = [
    path('fretes', FretesView.as_view(), name='fretes'),
]
