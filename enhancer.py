import os
import subprocess

class Enhancer:
    def __init__(self, input_dir="downloads/videos", output_dir="downloads/enhanced_videos"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def enhance_video(self, filename):
        input_path = os.path.join(self.input_dir, filename)
        output_path = os.path.join(self.output_dir, filename)

        if os.path.exists(output_path):
            print(f"Enhanced version already exists: {filename}")
            return True

        print(f"Enhancing {filename} ...")
        
        # FFmpeg command for basic enhancement:
        # - unsharp: Sharpening (luma_msize_x:luma_msize_y:luma_amount:chroma_msize_x:chroma_msize_y:chroma_amount)
        # - eq: Adjust contrast and saturation
        # - scale: Ensure it's at least 720p (optional but can help with clarity if combined with sharpening)
        
        command = [
            "ffmpeg", "-i", input_path,
            "-vf", "unsharp=5:5:1.0:5:5:0.0,eq=contrast=1.1:saturation=1.2",
            "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-c:a", "copy",
            output_path, "-y"
        ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            print(f"Successfully enhanced: {filename}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error enhancing {filename}: {e.stderr.decode()}")
            return False
        except FileNotFoundError:
            print("FFmpeg not found. Please ensure it is installed and in your PATH.")
            return False

    def enhance_all(self):
        if not os.path.exists(self.input_dir):
            print(f"Input directory {self.input_dir} does not exist.")
            return

        videos = [f for f in os.listdir(self.input_dir) if f.endswith(".mp4")]
        if not videos:
            print("No MP4 videos found to enhance.")
            return

        print(f"Found {len(videos)} videos. Starting enhancement process...")
        for video in videos:
            self.enhance_video(video)
        print("Enhancement process completed.")

if __name__ == "__main__":
    enhancer = Enhancer()
    enhancer.enhance_all()
