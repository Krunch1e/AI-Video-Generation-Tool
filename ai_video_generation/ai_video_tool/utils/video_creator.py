from moviepy.editor import ImageClip, AudioFileClip
import os

def create_video(image_path, audio_path):
    if not os.path.exists(audio_path):
        print(f"Audio file not found at {audio_path}")
        return

    image_clip = ImageClip(image_path).set_fps(24)
    audio_clip = AudioFileClip(audio_path)

    image_clip = image_clip.set_duration(audio_clip.duration)
    final_clip = image_clip.set_audio(audio_clip)

    final_clip.write_videofile(
        "assets/video.mp4",
        codec="libx264",
        audio_codec="libmp3lame",
        audio=True
    )
