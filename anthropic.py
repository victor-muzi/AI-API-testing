import os
from dotenv import load_dotenv
import anthropic


# Load your API key from .env file
load_dotenv()


client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))



message = client.messages.create(
    model="claude-3-haiku-20240307",
    system="Type in all caps always.",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello! I'm testing the API. Can you tell me a fun fact?"}
    ]
)


print(message.content[0].text)