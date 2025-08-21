import os
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



menssagem = client.responses.create(
    model="gpt-4.1-nano",
    instructions="Type in all caps always.",
    input=[
        {"role": "user", "content": "My favourite number is 81."},

    ],
)


print(menssagem.output_text)