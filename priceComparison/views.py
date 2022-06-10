from django.http import HttpResponse
from django.shortcuts import render
from . import sourceCode,microphoneInput
from django.http import JsonResponse
from shop.models import Product

def index(request):
    products = Product.objects.all()    #fetch products from database
    params = {'product':products} 
    return render(request, 'index.html', params)

def contact(request):
     return render(request, 'contact.html')

def productView(request):
    records = []
    productName = ""
    if request.method == 'POST':
        productName = request.POST.get('productName')
        records = sourceCode.main(productName)
        # print(records)
        
    return render(request, 'productView.html', {'productName':productName,'records':records})

def convertSpeechToText(request):
    print("Speech to text")
    #if request.method == 'GET':
    speech_text=microphoneInput.speechToText()
    return JsonResponse({'speech_text':speech_text})