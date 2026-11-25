from openai import OpenAI

# client = OpenAI(api_key="YOUR_FULL_API_KEY_HERE")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

SYSTEM = "You are a helpful grammar checking assistant."


# # Add this section to complete Task 3
# response = client.chat.completions.create(
#     model="gpt-6-luna",
#     messages=[
#         {"role": "system", "content": SYSTEM},
#         {"role": "user", "content": "She don't like apples."}
#     ]
# )

# print(response.choices[0].message.content)

# print((response.choices[0].message.content).strip())

def check_grammar(sentence):
   
    response = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": build_prompt(sentence)},
    ],
    temperature=0.2,
    max_tokens=200
)

    return (response.choices[0].message.content or "").strip()


def safe_correct(text):
    """Validate input and delegate to check_grammar; return friendly error on blank input."""
    text = (text or "").strip()
    if not text:
        return "Error: No text provided to correct."
    return check_grammar(text)


def build_prompt(text):
    return f'Correct the grammar in the following text:\n\n"{text}"'

    
while True:
    sentence = input("Enter a sentence: ").strip()
    if sentence.lower() == "q":
        print("Goodbye!") # Optional
        break
    result = safe_correct(sentence)
    print("Corrected version:")
    print(result, "\n")




