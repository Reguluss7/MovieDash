from core.views import hello_view, index
from django.urls import path

urlpatterns = [
    path('', hello_view, name='hello'),
    path('test', index, name='test')
]