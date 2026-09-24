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
prompt = "Write a short poem about the beauty of nature."

message = {
    "role": role,
    "content": prompt
}

messages = [message]
response = client.chat.completions.create(
    model=model,
    messages=messages
)
answer = response.choices[0].message.content
print("Response from the model:")
print(answer)
