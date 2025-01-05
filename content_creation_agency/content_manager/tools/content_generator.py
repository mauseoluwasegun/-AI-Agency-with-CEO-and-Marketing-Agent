from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

class content_generator(BaseTool):
    """
    A tool for generating content ideas using Anthropic's Claude model.
    It takes into account trends and content gaps to suggest new content ideas.
    """
    topic: str = Field(..., description="The main topic or area to generate content ideas for")
    content_gaps: str = Field(..., description="Content gaps identified from YouTube analysis")
    trends: str = Field(..., description="Current trending topics related to the main topic")
    youtube_performance: str = Field(..., description="Recent YouTube performance metrics")

    def run(self):
        """
        Generate content ideas using Anthropic's Claude model.
        """
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        prompt = f"""Based on the following information:
        Topic: {self.topic}
        Content Gaps: {self.content_gaps}
        Current Trends: {self.trends}
        YouTube Performance: {self.youtube_performance}
        
        Generate 5 unique and engaging content ideas that:
        1. Fill identified content gaps
        2. Leverage current trends
        3. Align with the main topic
        4. Consider past performance metrics
        
        For each idea, provide:
        - Title
        - Brief description
        - Target audience
        - Potential keywords
        - Estimated viewer interest (High/Medium/Low)
        - How it addresses content gaps
        - How it leverages current trends
        """
        
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=2000,
            temperature=0.7,
            system="You are a creative content strategist specializing in YouTube content creation. Your goal is to generate engaging content ideas that fill market gaps and leverage current trends.",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return message.content

if __name__ == "__main__":
    tool = content_generator(
        topic="Technology",
        content_gaps="Beginner-friendly tutorials, in-depth technical reviews",
        trends="AI tools, Productivity software",
        youtube_performance="Recent videos on software tutorials performing well, average 5k views"
    )
    print(tool.run()) 