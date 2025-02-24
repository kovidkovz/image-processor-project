from PIL import Image
import requests
from io import BytesIO
import os

async def compress_image(url: str, output_path: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(output_path, "JPEG", quality=50)  # Compress by 50%
        return output_path
    else:
        raise Exception(f"Failed to fetch image from {url}")
