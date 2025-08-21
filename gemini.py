import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


conversation_history = [
    types.Content(
        role="user", 
        parts=[types.Part.from_text(text="My favourite number is 81")]
    )
]

mensagem = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=conversation_history,
    config=types.GenerateContentConfig(system_instruction="Type in all caps.")
)


print(mensagem.text)