from django.urls import path
from .import views

urlpatterns = [
    path('disc/',views.disc,name='disc'),
]