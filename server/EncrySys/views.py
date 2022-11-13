from django.shortcuts import render
from django.views import generic
from django import views
from . import encodeDecode
# Create your views here.


def encrypt_view(request):
    if request.method == "POST":
        text = request.POST['my_textarea']
        output_text = encodeDecode.EncryptedState(text)
        return render(request,"encrypt.html",{"output_text":output_text,"input_text":text})
    else:
        return render(request,'encrypt.html')

def decrypt_view(request):
    if request.method == "POST":
        text = request.POST['my_textarea']
        output_text = encodeDecode.DecodedState(text)
        return render(request,"decrypt.html",{"output_text":output_text,"input_text":text})
    else:
        return render(request,'decrypt.html')