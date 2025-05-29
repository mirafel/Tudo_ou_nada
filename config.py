# -*- coding: utf-8 -*-
"""Configuration file for the 'Tudo ou nada' project."""

import os

# --- Google Cloud & Gemini API Configuration ---

# !!! IMPORTANT: Replace with your actual Gemini API Key !!!
# You can get one from Google AI Studio: https://aistudio.google.com/app/apikey
GEMINI_API_KEY = "AIzaSyBU2_q55uVwq22bgl378ufzaquF5T-GPgo" # Example: "AIzaSy..."

# !!! IMPORTANT: Replace with the full path to your Google Cloud credentials JSON file !!!
# This is needed for Google Cloud Speech-to-Text API.
# Example: r"C:\path\to\your\credentials.json" or "/home/user/path/to/credentials.json"
GOOGLE_APPLICATION_CREDENTIALS_PATH = r"C:\Users\felip\Desktop\Tudo_ou_nada\tudo-ou-nada-credencial.json"

# Optional: Google Cloud Project ID (sometimes needed for specific Cloud APIs)
# GOOGLE_CLOUD_PROJECT_ID = "your-project-id"

# --- Transcription & Language Configuration ---

# Language code for Google Cloud Speech-to-Text (e.g., "en-US", "pt-BR")
TRANSCRIPTION_LANGUAGE_CODE = "en-US"

# --- Gemini Model Configuration ---

# Choose the Gemini model to use for generating responses.
# Examples based on your available models:
# - "models/gemini-1.5-flash-latest"
# - "models/gemini-1.5-pro-latest"
# - "models/gemini-pro-vision" (if you plan image input)
# Make sure the chosen model is suitable for text generation.
GEMINI_MODEL_NAME = "models/gemini-1.5-flash-latest"

# --- Audio Configuration ---

# Sample rate for audio recording (Hz)
AUDIO_RATE = 16000
# Chunk size for audio streaming (affects latency)
AUDIO_CHUNK_SIZE = int(AUDIO_RATE / 10)  # 100ms chunks

# --- Interface Configuration ---

# Title for the Tkinter window
APP_TITLE = "Tudo ou Nada - Interview Assistant"

# --- Environment Setup --- 
# (This part sets the environment variable for Google Cloud libraries)

def setup_google_credentials():
    """Sets the GOOGLE_APPLICATION_CREDENTIALS environment variable."""
    if GOOGLE_APPLICATION_CREDENTIALS_PATH and os.path.exists(GOOGLE_APPLICATION_CREDENTIALS_PATH):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS_PATH
        print(f"Google Cloud Credentials set from: {GOOGLE_APPLICATION_CREDENTIALS_PATH}")
    elif "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
        print(f"Using existing GOOGLE_APPLICATION_CREDENTIALS environment variable.")
    else:
        print("WARNING: GOOGLE_APPLICATION_CREDENTIALS_PATH not set or file not found.")
        print("Google Cloud Speech-to-Text might not work without credentials.")

# You can call setup_google_credentials() at the start of your main.py

