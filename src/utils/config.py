import os
from dotenv import load_dotenv
import yaml

load_dotenv()

def load_config():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    config["groq_api_key"] = os.getenv("GROQ_API_KEY")
    config["news_api_key"] = os.getenv("NEWS_API_KEY")
    
    return config
