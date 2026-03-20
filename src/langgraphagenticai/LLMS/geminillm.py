import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI



class GeminiLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            GEMINI_API_KEY = self.user_controls_input["GEMINI_API_KEY"] 
            llm_model=self.user_controls_input["selected_gemini_model"]


            if GEMINI_API_KEY == "" and os.environ["GEMINI_API_KEY"] == '' :
                st.error("please give api key ")


            llm = ChatGoogleGenerativeAI(model = llm_model , api_key = GEMINI_API_KEY)

        except Exception as e:
            raise ValueError(f"hiiii occured with Exception : {e}")
        
        return llm






