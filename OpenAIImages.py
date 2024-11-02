import openai
from openai.types import ImagesResponse


class OpenAIImages:
    def __init__(self, client: openai.OpenAI):
        self.client = client
        self.model = 'dall-e-3'
        self.style='vivid'
        self.size='1024x1024'
        self.quality='standard'
        self.n=1
        self.last_response=None

    def get_last_response(self, n=0) -> str :
        return self.last_response.data[n].url if isinstance(self.last_response, ImagesResponse) else ''

    def execute_image_generating(self, user_prompt):
        params = {
            'model': self.model,
            'prompt': user_prompt,
            'style': self.style,
            'size': self.size,
            'quality': self.quality,
            'n': self.n,
        }

        params = {key: value for (key, value) in params.items() if value is not None}
        self.last_response = self.client.images.generate(**params)