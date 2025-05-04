import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import wave
import struct
import random
import os
# --- Cấu hình ---
width, height = 640, 480
fps = 30
duration_sec = 1
output_video = "random_video.avi"
output_audio = "random_audio.wav"
final_output = "final_video_with_audio.mp4"

# --- Tạo video không nén (MJPG để xem được bằng trình phát phổ biến) ---
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # gần như không nén, hỗ trợ tốt
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

for _ in range(fps * duration_sec):
    frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    out.write(frame)

out.release()
print(f"Video saved to {output_video}")

# --- Tạo âm thanh ngẫu nhiên ---
sample_rate = 44100
n_samples = duration_sec * sample_rate

with wave.open(output_audio, 'w') as wav_file:
    wav_file.setnchannels(1)         # mono
    wav_file.setsampwidth(2)         # 2 bytes per sample
    wav_file.setframerate(sample_rate)

    for _ in range(n_samples):
        value = random.randint(-32768, 32767)  # 16-bit PCM
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

print(f"Audio saved to {output_audio}")

# --- Ghép video + audio bằng moviepy ---
video_clip = VideoFileClip(output_video)
audio_clip = AudioFileClip(output_audio).set_duration(video_clip.duration)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(final_output, codec="libx264", audio_codec="aac")
os.remove(output_video)
os.remove(output_audio)
print(f"Final video with audio saved to {final_output}")

