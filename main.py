from litellm import completion
from dotenv import load_dotenv

load_dotenv()

openai_response = completion(
    model="gpt-4o-mini",
    messages=[
        {"content": "こんにちは！お元気ですか？", "role": "user"}
    ]
)

print(openai_response.choices[0].message.content)
