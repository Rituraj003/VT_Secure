from django.contrib import admin
from django.urls import path
from .views import EncryptView

urlpatterns=[
    path('',EncryptView.as_view(),name='encrypt_view')
]