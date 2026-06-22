from django.urls import path
from .views import complaint_view, track_complaint

urlpatterns = [
    path('', complaint_view, name='complaint'),
    path('track/', track_complaint, name='track'),
]