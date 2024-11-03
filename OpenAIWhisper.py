import openai
from openai.types.audio import Transcription


class OpenAIImages:
    def __init__(self, client: openai.OpenAI):
        self.client = client
        self.model = 'whisper-1'
        self.last_response=None

    def get_last_response(self,) -> str :
        return self.last_response.text if isinstance(self.last_response, Transcription) else ''

    def execute_image_generating(self, file_name):
        params = {
            'model': self.model,
            'file': file_name,
        }

        params = {key: value for (key, value) in params.items() if value is not None}
        self.last_response = self.client.audio.transcriptions.create(**params)