from utils.news_scraper import get_article, fetch_image
from utils.script_generator import generate_script
from utils.tts import generate_audio
from utils.video_creator import create_video

def main():
    # Get article
    title, description = get_article()
    print(f"Title: {title}")
    print(f"Description: {description}")

    # Fetch image for the video
    image_path = fetch_image(title)

    # Generate script for the video
    script = generate_script(title, description)
    print(f"Generated Script: {script}")

    # Generate the audio for the video
    audio_path = generate_audio(script)

    # Create the video by passing both image and audio paths
    create_video(image_path, audio_path)

if __name__ == "__main__":
    main()
