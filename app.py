import os
from langchain.agents import Tool
from langchain.llms import OpenAI
from langchain.utilities import SerpAPIWrapper
import streamlit as st

# Set API Keys
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "8a477f9b01a1bbf7e5ed8940940dae9d9cff7bc1ce01e868310823d4a724f502"  # Alternatively, load from .env

# Research Agent using SerpAPI
def research_agent(query):
    search = SerpAPIWrapper()
    return search.run(query)

# Use Case Generation Agent
def use_case_agent(industry_insights):
    llm = OpenAI(temperature=0.7)
    prompt = f"""
    Based on the following industry insights, generate 5 relevant AI/GenAI use cases:
    {industry_insights}
    """
    return llm(prompt)

# Streamlit App
st.title("Multi-Agent System for AI Use Case Generation")

company_or_industry = st.text_input("Enter a Company or Industry for Research")
if st.button("Generate Proposal"):
    st.write("Conducting research...")
    research = research_agent(company_or_industry)
    st.write(research)
