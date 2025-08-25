import os
from groq import GroqClient  

class GroqEmbedder:
    def __init__(self, api_key: str):
        self.client = GroqClient(api_key=api_key)

    def get_embedding_and_usage(self, text: str):
        response = self.client.embeddings.create(input=text, model="groq-embedding-ada-002")
        return response['data'][0]['embedding'], response['usage']
