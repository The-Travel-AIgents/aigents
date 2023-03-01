from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from app1.services import Guide
import json

# Create your views here.


class App1View(View):

    def post(self, request):

        body_bytes = request.body.decode('utf-8')
        body = json.loads(body_bytes)
        prompt = body.get('prompt')

        if not prompt:
            return JsonResponse({
                'success': False,
                'message': 'The prompt field is required.'
            }, status=400)

        response = Guide().generate(prompt=prompt)
        print(response)
        text = response.get('choices')[0].text

        return JsonResponse({
            'success': True,
            'message': 'Successfully generated guide',
            'data': {
                'text': text,
            }
        })


class WelcomeView(View):
    def get(self, request):
        return JsonResponse({
            'success': True,
            'message': 'Welcome to the Travel Aigent API'
        })
