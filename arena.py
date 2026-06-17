from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

def battle(prompt):

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    # Model A - Llama 3.3
    response_a = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer_a = response_a.choices[0].message.content

    # Model B - Llama 4 Scout
    response_b = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages
    )

    answer_b = response_b.choices[0].message.content

    print("\nMODEL A COMPLETED\n")
    print(answer_a[:200])

    print("\nMODEL B COMPLETED\n")
    print(answer_b[:200])


    return answer_a, answer_b