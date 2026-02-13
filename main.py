from groq import Groq

client = Groq(api_key="YOUR-GROQ-API-KEY")
messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"AI: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
