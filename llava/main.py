import base64
import logging
import os
from io import BytesIO

import requests
from PIL import Image
import cv2  # Import OpenCV

from langchain_community.llms import Ollama

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_image_or_first_frame_from_video(image_or_video_url):
    """
    Load an image from a URL or local path, or the first frame from a video.

    :param image_or_video_url: URL or local path to the image or video
    :return: PIL Image object
    """
    try:
        if image_or_video_url.startswith(('http://', 'https://')):
            response = requests.get(image_or_video_url, stream=True)
            response.raise_for_status()
            if 'video' in response.headers['Content-Type']:
                # It's a video, extract the first frame
                cap = cv2.VideoCapture(image_or_video_url)
                success, frame = cap.read()
                if success:
                    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    logger.error(f"Error extracting frame from video {image_or_video_url}")
                    return None
            else:
                # It's an image
                image = Image.open(BytesIO(response.content))
        else:
            # For local files, check extension
            if any(image_or_video_url.endswith(ext) for ext in ['.mp4', '.avi', '.mov']):  # Add other video formats as needed
                # It's a video file, extract the first frame
                cap = cv2.VideoCapture(image_or_video_url)
                success, frame = cap.read()
                if success:
                    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                else:
                    logger.error(f"Error extracting frame from video {image_or_video_url}")
                    return None
            else:
                # It's an image file
                image = Image.open(image_or_video_url)
        return image.convert('RGB')
    except Exception as e:
        logger.error(f"Error loading image or video {image_or_video_url}: {e}")
        return None

def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings.

    :param pil_image: PIL image
    :return: Base64 string
    """
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    # Example usage
    ollama_llm = Ollama(model="llava:34b-v1.6", base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"))
    
    media_urls = "http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1461818644od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3176574316od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1524759205od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m2492719933od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m765045042od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1757977306od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m2698345558od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m717783415od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m4035161360od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3356642309od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3012598894od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3527623903od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m430299995od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1228437345od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3454980520od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m632753883od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3826646243od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3839757711od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m2898256697od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m1312434917od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m87209101od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m4181416150od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m74854391od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m89998833od-w480_h360_x2.webp?w=1080&q=75, http://ap.rdcpix.com/f26d996a7895ac8ef8b44bc5628cce3bl-m3560213744od-w480_h360_x2.webp?w=1080&q=75".split(", ")

    for media_url in media_urls:
        logger.debug(f"Loading media {media_url}")
        media = load_image_or_first_frame_from_video(media_url.strip())
        if media:
            media_base64 = convert_to_base64(media)
            llm_with_media_context = ollama_llm.bind(images=[media_base64])
            logger.debug(f"Describing media {media_url}")
            response = llm_with_media_context.invoke("Describe this image in detail.")
            logger.info([media_url, response.strip()])

if __name__ == "__main__":
    main()
