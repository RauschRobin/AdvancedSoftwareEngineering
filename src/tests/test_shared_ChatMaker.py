from ..core.shared.Chat_GPT import Chat_Maker

def test_get_response_status():
    
    chat_obj = Chat_Maker()
    try:
        response = chat_obj.get_response("Write a tagline for an ice cream shop.")
        assert response != ''
    except:
        assert False
