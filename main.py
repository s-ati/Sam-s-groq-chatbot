from groq import Groq

client = Groq(api_key="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")
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
