import os
import subprocess

ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg")

# put path with videos here
video_folder = "c:\\projects\\FolderWithMP4Videos"

# list of supported extensions
video_extensions = [".mp4", ".mkv", ".avi"]

for file_name in os.listdir(video_folder):
    if os.path.splitext(file_name)[1].lower() in video_extensions:
        
        audio_file = os.path.splitext(file_name)[0] + ".wav"
        video_path = os.path.join(video_folder, file_name)
        audio_path = os.path.join(video_folder, audio_file)
        
        subprocess.run([ffmpeg_path, "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", "-y", audio_path], check=True)

        left_channel_file = os.path.splitext(file_name)[0] + "_left.wav"
        right_channel_file = os.path.splitext(file_name)[0] + "_right.wav"
        left_channel_path = os.path.join(video_folder, left_channel_file)
        right_channel_path = os.path.join(video_folder, right_channel_file)

        subprocess.run([ffmpeg_path, "-i", audio_path, "-map_channel", "0.0.0", "-ac", "1", "-ar", "44100", "-y", left_channel_path], check=True)
        subprocess.run([ffmpeg_path, "-i", audio_path, "-map_channel", "0.0.1", "-ac", "1", "-ar", "44100", "-y", right_channel_path], check=True)

        mixed_file = os.path.splitext(file_name)[0] + "_mixed.wav"
        mixed_path = os.path.join(video_folder, mixed_file)

        subprocess.run([ffmpeg_path, "-i", left_channel_path, "-i", right_channel_path, "-filter_complex", "[0:a][1:a]amerge=inputs=2,pan=mono|c0=c0+c1[aout]", "-map", "[aout]", "-y", mixed_path], check=True)

        os.remove(audio_path)
        os.remove(left_channel_path)
        os.remove(right_channel_path)

print("Done!")


