from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
    FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
    VOICE_ID = os.getenv("VOICE_ID") or "78ab82d5-25be-4f7d-82b3-7ad64e5b85b2"  # Default voice ID if not set

    @staticmethod
    def validate():
        if not Config.GOOGLE_API_KEY:
            raise ValueError("Missing GOOGLE_API_KEY in environment variables.")
        if not Config.CARTESIA_API_KEY:
            raise ValueError("Missing CARTESIA_API_KEY in environment variables.")
        if not Config.FIRECRAWL_API_KEY:
            raise ValueError("Missing FIRECRAWL_API_KEY in environment variables.")