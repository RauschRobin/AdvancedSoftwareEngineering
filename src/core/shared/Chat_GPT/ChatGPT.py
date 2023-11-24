import os

from dotenv import load_dotenv
from ...shared.YamlFetcher.YamlFetcher import YamlFetcher
from openai import OpenAI


class ChatGpt:
    """
    A class that represents a ChatGpt instance.

    Attributes:
        client (OpenAI): The OpenAI client used for API communication.

    Methods:
        __init__(): Initializes the ChatGpt instance.
        get_response(request): Generates a response using ChatGpt.

    """

    def __init__(self):
        """
        Initializes the ChatGPT class.
        """
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv('CHATGPT_SECRET')
        )

    def get_response(self, request):
        '''
        Gets a response, which is generated by ChatGPT.

        Parameters:
            request (string): The user's request.

        Returns:
            answer (string): The generated response.
        '''
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
