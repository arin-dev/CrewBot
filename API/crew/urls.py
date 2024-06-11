from django.urls import path, include
from . import views

urlpatterns = [
    path('crew_bot_endpoint/', views.crew_bot_endpoint),
    # path('push_dummy_data/', views.push_dummy_data),
]
