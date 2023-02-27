import openai
from django.conf import settings


class Guide:
    def __init__(self) -> None:
        openai.api_key = settings.OPENAI_API_KEY

    def generate(self, prompt):
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.2,
            max_tokens=150,
            frequency_penalty=0,
            presence_penalty=0.6,
            n=1,
        )
