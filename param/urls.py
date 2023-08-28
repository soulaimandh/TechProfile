from django.urls import path
from .views import get_sample_data

urlpatterns = [
    # Other URL patterns
    path('api/sample-data/', get_sample_data, name='get_sample_data'),
]
