import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_docs_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        result = response.choices[0].text.strip()

        if not result:
            raise ValueError("The GPT model returned an empty or incomplete response")

        return result

    except Exception as e:
        print(f"An error occurred while querying the GPT model: {e}")

    return None
