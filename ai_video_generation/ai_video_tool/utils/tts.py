import os
import requests
from dotenv import load_dotenv

load_dotenv()
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

def generate_audio(script_text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB/stream"

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": script_text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        audio_path = "assets/audio.mp3"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        print("Failed to generate audio:", response.text)
        return None
