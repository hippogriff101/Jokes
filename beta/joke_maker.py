from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



response = client.responses.create(
    model="gpt-5",
    input="Please write one funny joke that will make me and my friends laugh a lot, like not a roll eyes, a bawling on the floor."
)

print(response.output_text)