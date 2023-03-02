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

        dates_and_places = body.get('dates_and_places')  # day in place
        duration = body.get('duration')
        start_date = body.get('start_date')
        activities = body.get('activities')
        start_time = body.get('start_time')
        end_time = body.get('end_time')
        hotel_area = body.get('hotel_area')
        destination = body.get('destination')

        if not dates_and_places or not duration or not start_date or not activities or not start_time or not end_time or not hotel_area or not destination:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all the required fields.'
            }, status=400)

        customized_place_query = ''
        activities_query = ''

        for date_and_place in dates_and_places:
            customized_place_query += f'Please design the trip so that I spend the day of {date_and_place}. '

        for activity in activities:
            activities_query += f'{activity}'

        prompt = f'''
I want you to create a {duration} day trip starting on {start_date} for me in {destination}.  Please create a daily itinerary which includes the city I will be in (I can stay in the same city more than one day) and also what activities I'll do each day. Please include when I will travel between the various cities.
{customized_place_query}
What time will I leave and arrive?  Also how should I travel between the cities by car, train, plane, etc?
Please include which areas of each city I should stay in. 
I'd like to try {activities_query}.  Please include these activities on some of the days.
I prefer something near {hotel_area}, but not too noisy.  
Also if you have hotel recommendations to include, that would be helpful.  
Please include the start and end time of each activity.
I'd like to start my day at {start_time} and be finished by {end_time}.
        '''

        data = Guide().generate(prompt=prompt)

        return JsonResponse({
            'success': True,
            'message': 'Successfully generated guide',
            'data': data
        })


class WelcomeView(View):
    def get(self, request):
        return JsonResponse({
            'success': True,
            'message': 'Welcome to the Travel Aigent API'
        })
