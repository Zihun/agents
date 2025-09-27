
from openai import OpenAI

model_name = "gpt-4.1"
deployment = "gpt-4.1"

# Create an OpenAI client for Azure
client = OpenAI(
    api_key="BrCSq8oXpideyMkrm1TA8gzb5ptHzUCGgI9BX2eeMkIDt8u54ZEwJQQJ99BDACNns7RXJ3w3AAABACOGXpGL",
    #base_url="https://semiai-openai.openai.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2024-12-01-preview"
    base_url="https://semiai-openai.openai.azure.com/openai/"
)

# https://semiai-openai.openai.azure.com/openai/deployments/gpt-4.1/chat/completions?api-version=2024-12-01-preview

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "한국의 수도가 어디인가요?"}
    ],
    max_completion_tokens=13107,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment
)

print(response.choices[0].message.content)
