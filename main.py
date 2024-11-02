from OpenAIChat import OpenAIChat
from OpenAIImages import OpenAIImages
from OpenAIClient import OpenAIClient

client = OpenAIClient()

def execute_chat():
    chat = OpenAIChat(client.client)

    chat.execute_chat_completion('Tell me about Johann Sebastian Bach')
    print(chat.get_last_response())

def execute_image():
    image = OpenAIImages(client.client)
    image.execute_image_generating(' unicorns')
    print(image.get_last_response())


execute_image()