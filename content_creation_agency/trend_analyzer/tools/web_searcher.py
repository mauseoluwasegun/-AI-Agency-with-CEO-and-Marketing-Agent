from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

class WebSearcher(BaseTool):
    """
    A tool for searching the web using Tavily API to find trending topics
    and relevant content.
    """
    query: str = Field(..., description="The search query to find trending topics")
    max_results: int = Field(default=5, description="Maximum number of results to return")
    search_depth: str = Field(
        default="advanced",
        description="Search depth (basic or advanced)"
    )

    def run(self):
        """
        Search the web using Tavily API and return relevant results.
        """
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        response = client.search(
            query=self.query,
            search_depth=self.search_depth,
            max_results=self.max_results,
            include_answer=True,
            include_raw_content=False
        )
        
        # Format results
        result = f"Search Results for: {self.query}\n\n"
        
        if 'answer' in response and response['answer']:
            result += f"Summary: {response['answer']}\n\n"
        
        result += "Top Sources:\n"
        for i, article in enumerate(response.get('results', []), 1):
            result += f"\n{i}. {article['title']}\n"
            result += f"   URL: {article['url']}\n"
            if 'snippet' in article:
                result += f"   Summary: {article['snippet']}\n"
        
        return result

if __name__ == "__main__":
    tool = WebSearcher(
        query="latest trends in content creation 2024",
        max_results=3
    )
    print(tool.run()) 