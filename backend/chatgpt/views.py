from django.shortcuts import render
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def using_gpt():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do you make an alert appear after 10 seconds?\nJavaScript chatbot",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )

