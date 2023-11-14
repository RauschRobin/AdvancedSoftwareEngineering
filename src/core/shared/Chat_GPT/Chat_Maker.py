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


# from openai import OpenAI
# client = OpenAI()

# client.api_key = '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'

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)