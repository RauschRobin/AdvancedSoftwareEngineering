import openai

class ChatMaker:
    def __init__(self, maps_api_key):
        self.api_key = maps_api_key

    def get_response(self, request):
        response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=request
        )

        print(response.choices[0].text.strip())
        return response.choices[0].text.strip()
        
if __name__ == "__main__":
    myObj = ChatMaker('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')
    respones = myObj.get_response("Write a tagline for an ice cream shop.")
