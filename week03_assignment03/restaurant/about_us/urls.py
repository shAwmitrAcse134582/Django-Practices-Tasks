from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.about_us, name='about_us'),
]