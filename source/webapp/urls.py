from django.urls import path
from webapp.views import game

urlpatterns = [
    path('', game)
]
