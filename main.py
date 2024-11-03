from OpenAIChat import OpenAIChat
from OpenAIImages import OpenAIImages
from OpenAIClient import OpenAIClient
from OpenAITextToSpeech import OpenAITextToSpeech

client = OpenAIClient()

def execute_chat():
    chat = OpenAIChat(client.client)

    chat.execute_chat_completion('Tell me about Johann Sebastian Bach')
    print(chat.get_last_response())

def execute_image():
    image = OpenAIImages(client.client)
    image.execute_image_generating('Draw a picturesque landscape without text in August Leu style')
    print(image.get_last_response())
    image.save_last_response('Landscape_Leu.png')

def execute_image_variations():
    image = OpenAIImages(client.client)
    image.execute_image_variation('me_variation_variation.png')
    print(image.get_last_response())
    image.save_last_response('me_variation_variation_variation.png')

def execute_text_to_speech():
    tts = OpenAITextToSpeech(client.client)
    tts.execute_text_to_speech('Привіт?')

if __name__ == "__main__":
    execute_text_to_speech()