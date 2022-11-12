from django.shortcuts import render
from django.views import generic
# Create your views here.

class EncryptView(generic.TemplateView):
    template_name = "encrypt.html"