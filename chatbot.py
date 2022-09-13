import os
import openai

openai.api_key = "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" #genera tu propia api en openai!

conversation = ""

i = 1

while (i != 0):
    question = input("Humano: ")
    conversation += "\n Humano: " + question + "\nAI:"

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n Human:", " AI:"]
    )

    anwer = response.choices[0].text.strip()
    conversation += anwer
    print("AI: "+ anwer + "\sn" )