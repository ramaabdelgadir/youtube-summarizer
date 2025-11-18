import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str) -> str:
    """
    Extracts the YouTube video ID from various URL formats.
    (This is the robust regex version that handles all URL types)
    """
    patterns = [
        r"(?<=v=)[\w-]+",        # e.g., https://www.youtube.com/watch?v=...
        r"(?<=youtu\.be/)[\w-]+", # e.g., https://youtu.be/...
        r"(?<=embed/)[\w-]+"      # e.g., https://www.youtube.com/embed/...
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(0)
    
    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        video_ids = qs.get('v')
        if video_ids:
            return video_ids[0]
    except:
        pass 

    raise ValueError(f"Could not extract video ID from URL: {url}")

def get_transcript(video_url: str) -> str:
    """
    Fetch the transcript text of a YouTube video.
    (This uses your original, working `api.fetch` to prevent the crash)
    """
    try:
        video_id = extract_video_id(video_url)
        
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=['en', 'en-US', 'en-GB'])
        
        if not fetched:
            raise Exception("No transcript data was fetched (the list was empty).")


        full_text = " ".join([segment.text for segment in fetched])
        full_text = re.sub(r"\[.*?\]", "", full_text)
        full_text = re.sub(r"\s+", " ", full_text).strip()
        
        if not full_text:
             raise Exception("Transcript was empty after cleaning.")

        return full_text

    except Exception as e:
        if "No transcript found" in str(e):
            raise Exception("No English transcript found for this video.")
        raise Exception(f"Failed to get transcript: {e}")