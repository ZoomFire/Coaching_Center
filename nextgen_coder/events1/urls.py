from django.urls import path
from . import views

urlpatterns = [
    path('event1url/', views.events1, name='event1'),
]