from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.


class App1View(View):

    def get(self, request):
        return JsonResponse({
            'data': 'Hello world'
        })
