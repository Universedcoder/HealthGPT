"""Configuration settings for the HealthGPT application."""

# App settings
APP_CONFIG = {
    "page_title": "HealthGPT - Your AI Health Assistant",
    "page_icon": "🏥",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Theme colors
THEME = {
    "primary": "#3b82f6",
    "secondary": "#1d4ed8",
    "accent": "#60a5fa",
    "background": "#000000",
    "surface": "#1e293b",
    "text": "#e2e8f0",
    "text_secondary": "#94a3b8",
    "border": "#334155",
    "hover": "#2563eb"
}

# Model settings
MODEL_CONFIG = {
    "api_key": "google_genai",
    "model_name": "gemini-pro"
}

# Default user profile
DEFAULT_USER_PROFILE = {
    "name": "",
    "age": "",
    "gender": "",
    "conditions": [],
    "medications": [],
    "allergies": [],
    "last_checkup": ""
}
