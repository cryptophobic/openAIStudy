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

    #        Draw an isometric plan of kitchen in ISO 1046:1973.

    image.execute_image_generating('''
        Draw an isometric plan of kitchen in ISO 1046:1973. 
        Top-left conner of the room must bew in the top-left conner of image.
        Top-right conner of the room must bew in the top-right conner of image.
        Bottom-left conner of the room must bew in the bottom-left conner of image.
        Bottom-right conner of the room must bew in the bottom-right conner of image.
        ''')
    print(image.get_last_response())
    image.save_last_response()

def execute_image_variations():
    image = OpenAIImages(client.client)
    image.execute_image_variation('Study.png')
    print(image.get_last_response())
    image.save_last_response()

def execute_image_edit():
    image = OpenAIImages(client.client)
    image.execute_image_editing('Mitko.png', 'Mitko_mask.png', 'Photo of the happy ginger-bearded  man')
    print(image.get_last_response())
    image.save_last_response()

def execute_text_to_speech():
    tts = OpenAITextToSpeech(client.client)
    tts.execute_text_to_speech('Привіт?')

if __name__ == "__main__":
    execute_image_variations()