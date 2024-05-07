from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('portfolio-details',detales),
]
