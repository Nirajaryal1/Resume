import os
import requests
from urllib.parse import urlparse

class Downloader:
    def __init__(self, base_dir="downloads"):
        self.base_dir = base_dir
        self.image_dir = os.path.join(base_dir, "images")
        self.video_dir = os.path.join(base_dir, "videos")
        self.audio_dir = os.path.join(base_dir, "sounds")
        self._create_dirs()

    def _create_dirs(self):
        os.makedirs(self.image_dir, exist_ok=True)
        os.makedirs(self.video_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)

    def download_file(self, url, folder_type="images"):
        """
        Downloads a file from a URL and saves it to the specified folder.
        folder_type: "images", "videos", or "sounds"
        """
        if not url:
            print("No URL provided for download.")
            return False

        if folder_type == "images":
            target_dir = self.image_dir
        elif folder_type == "videos":
            target_dir = self.video_dir
        elif folder_type == "sounds":
            target_dir = self.audio_dir
        else:
            target_dir = self.image_dir
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            print(f"Could not determine filename from URL: {url}")
            return False

        file_path = os.path.join(target_dir, filename)

        # Skip if file already exists
        if os.path.exists(file_path):
            print(f"File already exists: {filename}")
            return True

        try:
            print(f"Downloading {url} ...")
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Saved: {file_path}")
            return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return False
