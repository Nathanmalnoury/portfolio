from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from contact import views

urlpatterns = [
    path("", views.contact, name='contact'),
    path("mail/", views.mail, name='mail'),
]

urlpatterns += staticfiles_urlpatterns()
