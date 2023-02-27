from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from app1.services import Guide

# Create your views here.


class App1View(View):

    def get(self, request):
        response = Guide().generate('Who is the president of the United States?')
        data = response.get('choices')[0].text
        return JsonResponse({
            'message': 'Successfully generated guide',
            'data': data
        })
