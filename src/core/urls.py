from core.views import hello_view
from django.urls import path

urlpatterns = [
    path('', hello_view, name='hello')
]