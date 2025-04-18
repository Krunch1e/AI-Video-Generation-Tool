import requests
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO

# Load the environment variables
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
PEXELS_API_URL = "https://api.pexels.com/v1/search"

def get_article():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    
    if data.get("articles"):
        article = data["articles"][0]
        title = article["title"]
        description = article["description"]
        return title, description
    else:
        return "No articles found", "No description available"

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def fetch_image(title, description):
    query = f"{title} {description} graphics card"
    params = {
        "engine": "google",
        "q": query,
        "tbm": "isch",
        "ijn": "0",
        "api_key": SERPAPI_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    if "images_results" not in data:
        print("No image results found.")
        return "assets/background.jpg"

    # Find first result with width >= 800
    for img in data["images_results"]:
        if int(img.get("original_width", 0)) >= 800:
            image_url = img["original"]
            break
    else:
        image_url = data["images_results"][0]["original"]

    # Download image
    img_data = requests.get(image_url).content
    img = Image.open(BytesIO(img_data))
    img_path = "assets/background.jpg"
    img.save(img_path)

    return img_path