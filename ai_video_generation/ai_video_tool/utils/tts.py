from gtts import gTTS
import os

def generate_audio(script):
    # Ensure the script is clean and doesn't contain extra prompt text
    script = script.strip()

    # Generate audio from the script
    tts = gTTS(text=script, lang='en')
    audio_path = "assets/audio.mp3"
    tts.save(audio_path)
    return audio_path
