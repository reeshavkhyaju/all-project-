from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

model = "gpt-6-luna"

user_prompt = input("Enter your prompt: ")
# user_prompt = "Tell me a joke in one line."

response = client.responses.create(model=model, input=user_prompt)

print(response.output_text)