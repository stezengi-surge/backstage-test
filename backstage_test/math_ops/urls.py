
from .views import DifferenceView
from django.urls import include, path

urlpatterns = [
    path("difference/", DifferenceView.as_view()),
]
