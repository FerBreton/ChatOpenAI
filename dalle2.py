import os 
import openai
from dotenv import load_dotenv

load_dotenv()

prompt = input("Ingresa un prompt: ")

openai.api_key = os.getenv("SECRET_KEY")
response = openai.Image.create(
    prompt = prompt,
    n=1,
    size="512x512"
)

print(response)