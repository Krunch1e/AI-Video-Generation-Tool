# AI News Video Generation Tool

This is a Python-based tool that automatically generates short videos from trending news articles. It scrapes the news, generates a script, converts it to human-like speech, selects a relevant background image, and compiles it all into a video.

---

## 🌟 Features

- **News Scraping:** Gets real-time trending news.
- **Script Generation:** Uses GPT-2 to generate a video script from the news.
- **Human-like TTS:** Converts the script to natural-sounding speech.
- **Smart Image Selection:** Uses Google (via SerpAPI) to find relevant images.
- **Video Compilation:** Combines image and audio into a video using MoviePy.

---

## 📂 Folder Structure

```
ai_video_tool/
├── main.py
├── utils/
│   ├── news_scraper.py
│   ├── script_generator.py
│   ├── tts.py
│   ├── video_creator.py
├── assets/
│   ├── background.jpg
│   ├── audio.mp3
│   └── video.mp4
├── .env
├── README.md
└── report.pdf
```

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Environment Variables
Create a `.env` or `key.env` file with:
```
NEWS_API_KEY=your_news_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here
```

### 3. Run the Project
```bash
python main.py
```

---

## 📊 Technologies Used
- Python
- OpenAI / DeepSeek / GPT-2 (Transformers)
- SerpAPI (Google Image Search)
- gTTS or ElevenLabs for TTS
- MoviePy (for video creation)

---

## 🔧 How It Works
1. **Scrape news** using `newsapi.org`
2. **Generate script** using a GPT-2 model
3. **Convert script to speech** using gTTS/ElevenLabs
4. **Find related image** using Google Images (via SerpAPI)
5. **Create video** using MoviePy

---

## 🎓 Future Improvements
- Support video overlays (text over image)
- Add subtitles
- Generate shortform (TikTok/YT Shorts) content
- Support multiple article batches per day
- Add GUI or web interface

---

## ✉️ Contact
**Developer:** Kartik Gaur  
Feel free to reach out if you'd like to collaborate or improve the project!

