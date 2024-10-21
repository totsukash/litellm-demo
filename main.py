from litellm import completion
from dotenv import load_dotenv
# import os

load_dotenv()

# OpenAI
# os.environ["OPENAI_API_KEY"] = "your-api-key"

# Anthropic
# os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

# Vertex AI
# os.environ["VERTEX_PROJECT"] = "hardy-device-386718"
# os.environ["VERTEX_LOCATION"] = "us-central1"

# HuggingFace
# os.environ["HUGGINGFACE_API_KEY"] = "huggingface_api_key"

# Azure
# os.environ["AZURE_API_KEY"] = ""
# os.environ["AZURE_API_BASE"] = ""
# os.environ["AZURE_API_VERSION"] = ""

response = completion(
    model="gpt-4o-mini",
    messages=[{"content": "こんにちは！お元気ですか？", "role": "user"}]
)

# HuggingFace API -----------------------------------
# response = completion(
#     model="huggingface/WizardLM/WizardCoder-Python-34B-V1.0",
#     messages=[{"content": "Hello, how are you?", "role": "user"}],
#     api_base="https://my-endpoint.huggingface.cloud"
# )

# Azure API -----------------------------------
# response = completion(
#     "azure/<your_deployment_name>",
#     messages=[{"content": "Hello, how are you?", "role": "user"}]
# )

# Ollama -----------------------------------
# response = completion(
#     model="ollama/llama2",
#     messages=[{"content": "Hello, how are you?", "role": "user"}],
#     api_base="http://localhost:11434"
# )

# OpenRouter -----------------------------------
# response = completion(
#     model="openrouter/google/palm-2-chat-bison",
#     messages=[{"content": "Hello, how are you?", "role": "user"}],
# )

print(response.choices[0].message.content)
