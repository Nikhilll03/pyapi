from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
'''while(1):
        text=input("Enter your text: ")
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=("text")
        break
     )
print(response.text)'''
while True:
    text = input("Enter your text: ")
    if text.lower() in ['exit', 'quit']:
        print("Exiting...")
        break
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[text]  # pass user input as a list
    )
    print("Gemini Output:", response.text)