from utils.news_scraper import get_article, fetch_image
from utils.script_generator import generate_script
from utils.tts import generate_audio
from utils.video_creator import create_video

def main():
    title, description = get_article()
    print(f"Title: {title}")
    print(f"Description: {description}")

    image_path = fetch_image(title, description)
    script = generate_script(title, description)
    print(f"Generated Script: {script}")

    audio_path = generate_audio(script)
    create_video(image_path, audio_path)

if __name__ == "__main__":
    main()
