from django.urls import path
from . import views

urlpatterns = [
    path('ad/',views.add_file),
    path('sb/',views.subtract_file),
]