from agency_swarm.tools import BaseTool
from pydantic import Field
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime, timedelta

class TrendAnalyzer(BaseTool):
    """
    A tool for analyzing Google Trends data using pytrends.
    It can analyze search trends and related queries for given keywords.
    """
    keywords: list = Field(..., description="List of keywords to analyze")
    timeframe: str = Field(
        default='today 3-m',
        description="Timeframe for the analysis (today 3-m, today 12-m, etc.)"
    )
    geo: str = Field(default='', description="Geographic location to analyze")

    def run(self):
        """
        Analyze trends using Google Trends API.
        """
        pytrends = TrendReq(hl='en-US', tz=360)
        
        # Build payload
        pytrends.build_payload(
            self.keywords,
            cat=0,
            timeframe=self.timeframe,
            geo=self.geo
        )
        
        # Get interest over time
        interest_over_time_df = pytrends.interest_over_time()
        
        # Get related queries
        related_queries = pytrends.related_queries()
        
        # Format results
        result = f"Trend Analysis for keywords: {', '.join(self.keywords)}\n\n"
        
        # Add interest over time summary
        result += "Interest Over Time:\n"
        for keyword in self.keywords:
            if keyword in interest_over_time_df.columns:
                avg_interest = interest_over_time_df[keyword].mean()
                max_interest = interest_over_time_df[keyword].max()
                result += f"\n{keyword}:\n"
                result += f"- Average Interest: {avg_interest:.2f}\n"
                result += f"- Peak Interest: {max_interest:.2f}\n"
        
        # Add related queries
        result += "\nRelated Queries:\n"
        for keyword in self.keywords:
            if keyword in related_queries:
                result += f"\n{keyword}:\n"
                # Top queries
                if 'top' in related_queries[keyword] and not related_queries[keyword]['top'].empty:
                    result += "Top Queries:\n"
                    for _, row in related_queries[keyword]['top'].head(5).iterrows():
                        result += f"- {row['query']}: {row['value']}\n"
                # Rising queries
                if 'rising' in related_queries[keyword] and not related_queries[keyword]['rising'].empty:
                    result += "\nRising Queries:\n"
                    for _, row in related_queries[keyword]['rising'].head(5).iterrows():
                        result += f"- {row['query']}: {row['value']}\n"
        
        return result

if __name__ == "__main__":
    tool = TrendAnalyzer(
        keywords=["content creation", "youtube tutorial"],
        timeframe='today 3-m'
    )
    print(tool.run()) 