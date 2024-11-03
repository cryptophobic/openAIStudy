import openai
from openai.types.audio import Transcription


class OpenAITextToSpeech:
    def __init__(self, client: openai.OpenAI):
        self.client = client
        self.model = 'tts-1'
        self.voice = 'alloy'
        self.last_response=None

    def get_last_response(self,) -> str :
        return self.last_response.text if isinstance(self.last_response, Transcription) else ''

    def execute_text_to_speech(self, text):
        params = {
            'model': self.model,
            'voice': self.voice,
            'input': text,
        }

        params = {key: value for (key, value) in params.items() if value is not None}
        with self.client.audio.speech.with_streaming_response.create(**params) as self.last_response:
            self.last_response.stream_to_file(f'generated/output.mp3')