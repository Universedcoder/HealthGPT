"""Utility functions for the HealthGPT application."""

import html
from typing import Dict
import streamlit as st
import google.generativeai as genai
from config import MODEL_CONFIG

def sanitize_message(text: str) -> str:
    """Sanitize message content and convert newlines to HTML line breaks."""
    sanitized = html.escape(text)
    return sanitized.replace('\n', '<br>')

def generate_healthcare_prompt(input_text: str, user_data: Dict) -> str:
    """Generate a healthcare-specific prompt with user context."""
    return (
        f"You are HealthGPT, an AI healthcare assistant. Provide accurate, concise healthcare-related responses.\n"
        f"User Details:\n"
        f"Name: {user_data['name']}\n"
        f"Age: {user_data['age']}\n"
        f"Gender: {user_data['gender']}\n"
        f"Conditions: {', '.join(user_data['conditions'])}\n"
        f"Medications: {', '.join(user_data['medications'])}\n"
        f"Allergies: {', '.join(user_data['allergies'])}\n"
        f"Last Checkup: {user_data['last_checkup']}\n"
        f"Question: {input_text}"
    )

def get_ai_response(input_text: str, user_data: Dict) -> str:
    """Generate AI response using the Gemini API."""
    try:
        if not MODEL_CONFIG["api_key"]:
            st.error("Please set your Gemini API key in config.py")
            return "Please set your Gemini API key in config.py"
        genai.configure(api_key=MODEL_CONFIG["api_key"])
        model = genai.GenerativeModel(MODEL_CONFIG["model_name"])
        prompt = generate_healthcare_prompt(input_text, user_data)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I apologize, but I'm having trouble generating a response right now. Please try again in a moment."
