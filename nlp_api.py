
import paralleldots

class API:

    def __init__(self):
        api_key = '' # put your own parallel dots api key
        paralleldots.set_api_key(api_key)

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self, text):
        response = paralleldots.ner(text)
        return response

    def emotion_analysis(self, text):
        response = paralleldots.emotion(text)
        return response
