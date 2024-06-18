from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def blog_list(request):
    data = {
        "Message": "Hello World"
    }
    
    return JsonResponse(data)
