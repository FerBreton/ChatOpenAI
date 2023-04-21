import os 
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("SECRET_KEY")

audio_file = open("files/test.m4a", "rb")

transcipt = openai.Audio.transcribe("whisper-1", audio_file)

words = transcipt["text"]

print(words)



print("Si lo encontre") if "Primera" in words else print("No ta")