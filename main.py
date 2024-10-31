import os
from openai import OpenAI
from config import OPENAI_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

client = OpenAI()
# for model in client.models.list():
#     print(model)

system_role_content = ('You are helpful assistance')

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': system_role_content},
        {'role': 'user', 'content': 'Write a short article about Norse Mythology gods'},
    ],
    temperature=1,
    # seed=1234
    # top_p=0.1,
    # max_tokens=10,
    # n=2,
    # stop=[';', '.'],
    frequency_penalty=0,  # between -2 and 2, default 0
    presence_penalty=0,  # between -2 and 2, default 0

)

print(response.choices[0].message.content)