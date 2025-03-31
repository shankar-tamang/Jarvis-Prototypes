from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class Orchestrator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    def filtered_response(self, unfiltered_text):
        pass

    def generate(self, speaker_text):
        response_unfiltered = self.llm.invoke(speaker_text).content
        response = response_unfiltered.replace("*", "")
        return response
    

