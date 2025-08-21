import os
from dotenv import load_dotenv
import anthropic
from config import CONFIG


load_dotenv()


client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))



mensagem = client.messages.create(
    model="claude-3-haiku-20240307",
    system=CONFIG["system_instruction"],
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello! I'm testing the API. Can you tell me a fun fact?"}
    ]
)


print(mensagem.content[0].text)