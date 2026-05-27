from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

for i in range(2):
    #Code inside this loop will keep on running until manually stopped
    question = input("You (Press 'exit' or 'quit' to stop): ")

    if question.lower() in ["exit", "quit"]:
        break

    print("Thinking...\n")
    response = client.chat.completions.create(
        model="baidu/cobuddy:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful educational tutor."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.choices[0].message.content

    print("\nAI:", answer)
    print("\n-------------------\n")