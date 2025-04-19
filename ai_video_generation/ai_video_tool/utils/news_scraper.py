import requests
import os
import random
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
PEXELS_API_URL = "https://api.pexels.com/v1/search"

def get_article():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'us',
        'pageSize': 15  # Get top 15 headlines
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    articles = data.get("articles", [])
    valid_articles = [
        article for article in articles 
        if article.get("title") and article.get("description")
    ]

    if valid_articles:
        article = random.choice(valid_articles)
        title = article["title"]
        description = article["description"]
        return title, description
    else:
        return "No articles found", "No description available"

def fetch_image(title, description):
    query = f"{title} {description}"
    params = {
        "engine": "google",
        "q": query,
        "tbm": "isch",
        "ijn": "0",
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        if "images_results" not in data or not data["images_results"]:
            print("No image results found.")
            return "assets/default_background.jpg"

        # Find a large image or fallback to the first one
        image_url = None
        for img in data["images_results"]:
            if int(img.get("original_width", 0)) >= 800:
                image_url = img["original"]
                break
        else:
            image_url = data["images_results"][0]["original"]

        # Download and save the image
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))
        img_path = "assets/background.jpg"
        img.save(img_path)
        return img_path

    except Exception as e:
        print(f"Error fetching image: {e}")
        return "assets/default_background.jpg"
