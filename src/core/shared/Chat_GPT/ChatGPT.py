from ...shared.YamlFetcher.YamlFetcher import YamlFetcher
from openai import OpenAI

class ChatGpt:
    def __init__(self):
        self.client = OpenAI(
            api_key=YamlFetcher.fetch("chatgpt", "API_Keys.yaml")
        )
        
    def get_response(self, request):
        '''
        Gets a response, which is generated by ChatGPT.

        Parameters: request
        Returns: answer (string)
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