from django.urls import path
from .views import message_view

urlpatterns = [
    path('', message_view, name='message'),
]
