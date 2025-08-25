import streamlit as st
from agents.news_scraper import NewsSpiderAgent
from agents.voice_reader import NewsVoiceAgent
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(
        page_title="Ora: The Voice of News",
        page_icon="🎙️",
        layout="wide"
    )
    
    st.title("Ora: The Voice of News")
    st.markdown("""
                ### 🛠 How to Use Ora
                1. **Choose a news category** from the sidebar.
                2. Click **'Get News'** to fetch the latest headlines.
                3. Wait for few seconds – Ora will read the news for you with an AI voice!
                
                ---
            """)
    st.sidebar.header("Select News Category")

    categories = ["Latest", "Politics", "Sports", "Business", "Entertainment", "India", "World", "Lifestyle"]

    category_choice = st.sidebar.selectbox("Choose a category:", categories)
    
    if st.sidebar.button("Get News"):
        with st.spinner(f"🔄 Generating news for category: {category_choice.title()}..."):
            
            # Create spider agent for scraping
            spider_agent = NewsSpiderAgent()
            news_data = spider_agent.scrape_category_news(category_choice)
            
            if news_data:
                st.success(f"✅ Successfully fetched {category_choice} news!")
                
                # Display news in expandable sections
                with st.expander("📰 View News Articles", expanded=False):
                    st.write(news_data)
                
                # Generate audio
                with st.spinner("Generating audio..."):
                    voice_agent = NewsVoiceAgent()
                    audio_response = voice_agent.read_news(news_data, category_choice)
                    
                    if audio_response:
                        # Get audio bytes directly (no file saving)
                        # If NewsVoiceAgent has a save_audio method that returns a file path, read bytes from the file
                        audio_file = voice_agent.save_audio(audio_response)
                        
                        if audio_file and os.path.exists(audio_file):
                            with open(audio_file, "rb") as f:
                                audio_bytes = f.read()
                            st.audio(audio_bytes, format='audio/mp3')
                            st.success("🎵 News audio generated successfully!")
                        else:
                            st.error("❌ Failed to process audio.")
                    else:
                        st.error("❌ Failed to generate audio.")
            else:
                st.error("❌ Failed to scrape news. Please try again.")

    st.markdown("""
                **Made with ❤️ using [Agno](https://agno.ai), [FireCrawl](https://firecrawl.dev), and [Cartesia](https://cartesia.ai)**  
                By [Shivam Katare](https://github.com/Shivam-Katare)
                """)

if __name__ == "__main__":
    main()