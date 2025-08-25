from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.cartesia import CartesiaTools
from agno.utils.audio import write_audio_to_file
import os

class NewsVoiceAgent:
    def __init__(self, agent_name: str = "Ora"):
        self.agent_name = agent_name
        self.agent = Agent(
            name="Professional News Reader",
            model=Gemini(id="gemini-2.0-flash-lite"),
            tools=[CartesiaTools(
                default_voice_id="6f84f4b8-58a2-430c-8c79-688dad597532",
                list_voices_enabled=True
            )],
            instructions=[
                f"You are a professional news anchor named '{agent_name}'",
                "Generate short, concise audio summaries",
                "Keep audio under 45 seconds for faster processing",
                "Focus on key points only",
                "Use clear and engaging voice"
            ],
            show_tool_calls=True
        )
    
    def read_news(self, news_data: str, category: str = "latest"):
        """
        Convert news data to speech using Cartesia
        """
        # Extract up to 5 titles for a comprehensive summary
        lines = news_data.split('\n')
        titles = []
        
        for line in lines:
            # Check for multiple possible title formats
            if '**Title:**' in line or 'News title:' in line or 'News Title:' in line or 'Title:' in line:
                # Clean up the title by removing various prefixes
                title = line.replace('**Title:**', '').replace('News title:', '').replace('News Title:', '').replace('Title:', '').strip()
                if title and len(titles) < 5:  # Limit to 5 headlines
                    titles.append(title)
        
        print("DEBUG - Raw news data:", news_data[:500])  # Debug first 500 chars
        print("DEBUG - Extracted titles:", titles)
        
        # Create a professional NYC evening news style script
        if titles:
            print("titles=========", titles)
            short_script = f"""
            Hello everyone, I'm {self.agent_name} with your {category} news update.
    
            The first story comes from Indian Express: {titles[0] if len(titles) > 0 else 'No news available'}.
    
            In other news, {titles[1] if len(titles) > 1 else ''}.
    
            Meanwhile, {titles[2] if len(titles) > 2 else ''}.
    
            Also making headlines today, {titles[3] if len(titles) > 3 else ''}.
    
            And finally, {titles[4] if len(titles) > 4 else ''}.
    
            That's your news update. I'm {self.agent_name}, thank you for joining us.
            """
        else:
            short_script = f"Hello, this is {self.agent_name}. No {category} news available at the moment. Thank you for listening."
        
        prompt = f"Convert this short news summary to speech using text-to-speech: {short_script.strip()}"
        
        try:
            # Remove stream=True to get proper response object
            response = self.agent.run(prompt)
            return response
        except Exception as e:
            print(f"Error generating voice: {str(e)}")
            return None
    
    def get_audio_bytes(self, response):
        """
        Get audio bytes for direct playback in Streamlit
        """
        if response and hasattr(response, 'audio') and response.audio:
            try:
                import base64
                base64_audio = response.audio[0].base64_audio
                audio_bytes = base64.b64decode(base64_audio)
                return audio_bytes
            except Exception as e:
                print(f"Error processing audio: {str(e)}")
                return None
        return None
    
    def save_audio(self, response, filename: str = "News"):
        """
        Save the generated audio to file
        """
        if response and hasattr(response, 'audio') and response.audio:
            try:
                if not filename.endswith('.mp3'):
                    filename = f"{filename}.mp3"
                
                write_audio_to_file(
                    response.audio[0].base64_audio,
                    filename=filename
                )
                return filename
            except Exception as e:
                print(f"Error saving audio: {str(e)}")
                return None
        return None