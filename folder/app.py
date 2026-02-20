import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit UI
st.title("🍲 Flavour Fusion: AI-Driven Recipe Blogging")

recipe_topic = st.text_input("Enter Recipe Topic")
word_count = st.number_input("Enter Word Count", min_value=300, max_value=2000, step=100)

if st.button("Generate Recipe Blog"):

    model = genai.GenerativeModel("gemini-pro")

    # Recipe Prompt
    prompt = f"""
    Write a detailed {word_count}-word blog post about {recipe_topic}.
    Include:
    - Introduction
    - Ingredients
    - Step-by-step instructions
    - Tips
    - Conclusion
    Make it engaging and creative.
    """

    # Generate Recipe
    response = model.generate_content(prompt)

    # Generate Programmer Joke
    joke_prompt = "Tell me a short funny programmer joke."
    joke_response = model.generate_content(joke_prompt)

    st.subheader("🤣 Programmer Joke While You Wait")
    st.write(joke_response.text)

    st.subheader("📝 Your AI-Generated Recipe Blog")
    st.write(response.text)
