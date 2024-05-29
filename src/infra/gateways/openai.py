import os
import openai


class OpenAI:
    def __init__(self):
        self.openai = openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")
        print(self.openai.Model.list())
