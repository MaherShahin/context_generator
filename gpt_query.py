"""
This module provides functionality for querying OpenAI GPT models 
and generating summarized documentation.
"""

import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class GPTQuery:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def _query(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )

            result = response["choices"][0]["message"]["content"]

            if not result:
                raise ValueError("The GPT model returned an empty or incomplete response")

            return result

        except Exception as e:
            print(f"An error occurred while querying the GPT model: {e}")

        return None

    def generate_docs_gpt(self, messages):
        """
        Generates documentation using the OpenAI GPT model by sending a list of messages.

        Args:
            messages (list): A list of messages to be sent to the GPT model.

        Returns:
            str: The generated documentation.
        """
        return self._query(messages)

    def generate_summarized_doc(self, docstrings):
        """
        Generates summarized documentation for a list of docstrings.

        Args:
            docstrings (list): A list of docstrings to be summarized.

        Returns:
            list: A list of summarized documentation.
        """
        summarized_docs = []
        # TODO: Implement this method
        return summarized_docs
