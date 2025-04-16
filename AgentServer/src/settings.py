from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
class Settings(BaseSettings):
    OUTPUT_PATH: str
    GOOGLE_API_KEY: str
    MODEL: str
    API_PORT: str
    SYSTEM_INSTRUCTION: str

SETTINGS = Settings()
