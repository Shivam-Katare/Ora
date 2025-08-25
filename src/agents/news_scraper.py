from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.firecrawl import FirecrawlTools

class NewsSpiderAgent:
    def __init__(self):
        self.agent = Agent(
            name="Indian Express News Scraper",
            model=Gemini(id="gemini-2.0-flash-lite"),
            tools=[FirecrawlTools()],
            instructions=[
                "You are a specialized news scraper for Indian Express website",
                "Extract news articles with title, summary, and source information",
                "Focus on getting the most recent and relevant news",
                "Format the output in a structured way for voice reading",
                "Ensure all extracted content is clean and readable"
            ],
            show_tool_calls=True
        )
    
    def scrape_category_news(self, category: str, num_articles: int = 5):
        """
        Scrape news from Indian Express based on category
        """
        base_url = "https://indianexpress.com/"
        
        # Map categories to URL paths
        category_urls = {
            "Latest": base_url,
            "Politics": f"{base_url}section/political-pulse/",
            "Sports": f"{base_url}section/sports/",
            "Business": f"{base_url}section/business/",
            "Entertainment": f"{base_url}section/entertainment/",
            "India": f"{base_url}section/india/",
            "World": f"{base_url}section/world/",
            "Lifestyle": f"{base_url}section/lifestyle/"
        }
        
        target_url = category_urls.get(category, base_url)
        
        prompt = f"""
        Scrape the {category} news from {target_url} and extract exactly {num_articles} news articles.
        
        For each article, provide:
        1. News title
        2. Brief summary (2-3 sentences)
        3. Source (Indian Express)
        
        Format the response as a clean, structured text that can be easily read by a voice agent.
        Focus on the most important and recent news items.
        """
        
        try:
            response = self.agent.run(prompt)
            return response.content if response else None
        except Exception as e:
            print(f"Error scraping news: {str(e)}")
            return None