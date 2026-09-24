import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
env_path = Path(__file__).parent.parent.parent / ".env"

load_dotenv(env_path)

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "suggest a clothing brand company name and only suggest 1 name"

message_system = {
    "role": "system",
    "content": "you are a brand manager who suggest a name for my company and also suggest a tagline for the company. you are also a copywriter who can write a short description about the company."
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.1,
)
answer = response.choices[0].message.content
print("Response from the model:")
print(answer)
