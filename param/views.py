from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def get_sample_data(request):
    data = {'message': 'This is sample data from the Django main app.'}
    return JsonResponse(data)
