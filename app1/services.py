import openai
import json
from django.conf import settings


class Guide:
    def __init__(self) -> None:
        openai.api_key = settings.OPENAI_API_KEY

    def generate(self, prompt):

        openai_response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': '''
You are an AI travel agent. All your response should be in nothing but a key-value JSON format. Do not add any newline(i.e / n) between your response. Do not add any other text other than the JSON response. Format the JSON in the following format:
{
"trip":
    "city_itinerary": [
        "activities": [
            {
                "name": "",
                "start_time": "",
                "end_time": "",
                "location": ""
            }
        ],
        "area_to_stay": "",
        "city": "",
        "date": ""
        "hotel_recommendation": {
            "name": "",
            "location": "",
            "rating": "",
            "contact": {
                "phone": "",
                "email": "",
                "website": ""
            }
        }
    ],
    "travel_itinerary": {},
    "end_date": "",
    "start_date": "",
    "destination": "",
    "additional_info": ""
}
                            '''
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        response = openai_response['choices'][0]['message']['content']

        print(response)

        return json.loads(response)
