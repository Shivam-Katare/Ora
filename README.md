# Ora: The Voice of News 🎙️


https://github.com/user-attachments/assets/62c93ec8-8162-42d2-8a9c-91009a3ce498



Ora is an AI-powered news reader that fetches the latest headlines from Indian Express and converts them into professional news broadcasts using AI voice synthesis. Just pick a category, hit a button, and let Ora read the news to you!

## ✨ Features

- 🎯 **Multi-category news**: Latest, Politics, Sports, Business, Entertainment, India, World, Lifestyle
- 🎙️ **AI voice synthesis**: Professional female news anchor voice using Cartesia
- 📱 **Clean UI**: Dark theme Streamlit interface
- ⚡ **Real-time scraping**: Fresh news directly from Indian Express
- 🎵 **Audio playback**: Listen to news directly in your browser

## 🛠️ Tech Stack

- **[Agno](https://docs.agno.com/introduction)** - AI agent framework
- **[FireCrawl](https://firecrawl.dev)** - Web scraping
- **[Cartesia](https://cartesia.ai)** - Voice synthesis
- **[Streamlit](https://streamlit.io)** - Web interface

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd news-agent-streamlit
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API keys
Create a `.env` file in the project root and add your API keys:

```bash
GOOGLE_API_KEY="your_google_gemini_api_key_here"
export CARTESIA_API_KEY="your_cartesia_api_key_here"
FIRECRAWL_API_KEY="your_firecrawl_api_key_here"
```

**Important**: Note the `export` prefix for the Cartesia API key - this is required.

### 4. Run the app
```bash
streamlit run src/app.py
```

The app will open in your browser at `http://localhost:8501`

## 🔑 API Keys Setup

You'll need to get API keys from these services:

### Google Gemini API
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key to your `.env` file

### Cartesia API
1. Visit [Cartesia](https://cartesia.ai)
2. Sign up for an account
3. Generate an API key from your dashboard
4. Add it to `.env` with the `export` prefix

### FireCrawl API
1. Go to [FireCrawl](https://firecrawl.dev)
2. Create an account
3. Get your API key from the dashboard
4. Add it to your `.env` file

## 📖 How to Use

1. **Choose a category** from the sidebar dropdown
2. Click **"Get News"** to fetch latest headlines
3. Wait a few seconds for Ora to generate the audio
4. Listen to your personalized news broadcast!

## 📁 Project Structure

```
news-agent-streamlit/
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── agents/
│   │   ├── news_scraper.py # News scraping agent
│   │   └── voice_reader.py # Voice synthesis agent
│   ├── components/         # UI components
│   └── utils/             # Utility functions
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── requirements.txt       # Python dependencies
├── .env                   # API keys (create this)
└── README.md             # This file
```

## 🔄 Current Limitations

- Single news source (Indian Express only)
- One voice option
- English language only
- 
## 🚧 Upcoming Features

- [ ] Multiple news sources
- [ ] Different voice options
- [ ] Multi-language support

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Areas for improvement:

- Add more news sources
- Implement different voice styles
- Improve UI/UX
- Add caching for faster performance
- Add tests

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♀️ Support

If you encounter any issues:

1. Check that all API keys are correctly set in `.env`
2. Ensure you have stable internet connection
3. Verify all dependencies are installed
4. Check the terminal for error messages

## 💫 Made with ❤️
---

**Enjoy your personalized AI news experience with Ora!**
