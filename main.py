import os
from openai import OpenAI
from config import OPENAI_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

client = OpenAI()
# for model in client.models.list():
#     print(model)

system_role_content = ('Format output the way where the max line length is 80 characters')

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': system_role_content},
        {'role': 'user', 'content': 'Please tell me a short English story'},
    ]
)
print(response.choices[0].message.content)