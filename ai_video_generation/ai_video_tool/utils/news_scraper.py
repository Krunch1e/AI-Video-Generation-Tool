import requests
from dotenv import load_dotenv
import os

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

def fetch_image(title):
    # Use Pexels API to fetch a relevant image based on the article's title
    headers = {
        'Authorization': PEXELS_API_KEY
    }
    params = {
        'query': title,
        'per_page': 1
    }
    response = requests.get(PEXELS_API_URL, headers=headers, params=params)
    data = response.json()

    if data.get('photos'):
        # Get the first image from the search results
        image_url = data['photos'][0]['src']['original']
        img_data = requests.get(image_url).content
        image_path = 'assets/background.jpg'
        with open(image_path, 'wb') as handler:
            handler.write(img_data)
        return image_path
    else:
        return 'assets/background.jpg'  # Default image if no result is found
