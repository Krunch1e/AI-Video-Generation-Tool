from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
import os

def create_video(image_path, audio_path):
    # Load background image
    image_clip = ImageClip(image_path).set_duration(10)  # temporary duration, will match audio later
    image_clip = image_clip.set_fps(24)

    # Load audio file
    if not os.path.exists(audio_path):
        print(f"Audio file not found at {audio_path}")
        return

    audio_clip = AudioFileClip(audio_path)

    # Set video duration to match audio duration
    image_clip = image_clip.set_duration(audio_clip.duration)

    # Attach the audio to the video
    final_clip = image_clip.set_audio(audio_clip)

    # Export the video with audio embedded
    final_clip.write_videofile(
        "assets/video.mp4",
        codec="libx264",
        audio_codec="libmp3lame",  # more reliable in 1.0.3
        audio=True
    )
