from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

model = "gpt-6-luna"


system_prompt = "You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Use emojis only."

user_prompt = input("Enter your prompt: ")

messages = [
    {
        "role": "system",
        "content": [
            {
                "type": "input_text",
                "text": system_prompt
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": user_prompt
            }
        ]
    },
]
# user_prompt = "Tell me a joke in one line."


response = client.responses.create(
    model=model,
    input=messages
)
# response = client.responses.create(model=model, input=user_prompt)

print(response.output_text)