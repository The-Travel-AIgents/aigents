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
                'message': 'The prompt field is required.'
            }, status=400)

        try:
            response = Guide().generate(prompt=prompt)
            data = response.get('choices')[0].text
        except:
            return JsonResponse({
                'message': 'An internal server error occured.'
            })

        return JsonResponse({
            'message': 'Successfully generated guide',
            'data': data
        })
