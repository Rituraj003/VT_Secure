from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.encrypt_view ,name='encrypt_view'),
    path('/decrypt',views.decrypt_view, name="decrypt_view")
]