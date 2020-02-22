from django.urls import path

from aboutme import views

urlpatterns = [
    path("", views.section, name='aboutme'),
]
