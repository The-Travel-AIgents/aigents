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
                    'content': 'You are an AI travel agent. All your response should be in a key-value JSON format. Format the JSON in such a way that the result can be used programmatically. Do not add any newline (i.e /n) between your response.'
                },
                {'role': 'user', 'content': prompt}
            ]
        )

        response = openai_response['choices'][0]['message']['content']

        return json.loads(response)
