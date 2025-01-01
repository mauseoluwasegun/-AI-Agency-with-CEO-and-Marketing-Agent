from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from textblob import TextBlob

load_dotenv()

class CompetitorAnalyzer(BaseTool):
    """
    A tool for analyzing competitor channels and identifying content gaps.
    It analyzes competitor videos, engagement rates, and content strategies.
    """
    keywords: list = Field(..., description="List of keywords to search for competitor content")
    max_results: int = Field(default=10, description="Maximum number of videos to analyze per keyword")

    def run(self):
        """
        Analyze competitor channels and content gaps.
        """
        youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
        
        result = "Competitor Analysis Report\n\n"
        all_videos = []
        
        # Search for videos for each keyword
        for keyword in self.keywords:
            search_response = youtube.search().list(
                q=keyword,
                part='id,snippet',
                maxResults=self.max_results,
                type='video',
                order='viewCount'
            ).execute()
            
            result += f"\nTop Videos for '{keyword}':\n"
            
            for item in search_response.get('items', []):
                video_id = item['id']['videoId']
                
                # Get video statistics
                video_stats = youtube.videos().list(
                    part='statistics,contentDetails',
                    id=video_id
                ).execute()
                
                if video_stats['items']:
                    stats = video_stats['items'][0]['statistics']
                    
                    # Calculate engagement rate
                    views = int(stats.get('viewCount', 0))
                    likes = int(stats.get('likeCount', 0))
                    comments = int(stats.get('commentCount', 0))
                    engagement_rate = ((likes + comments) / views * 100) if views > 0 else 0
                    
                    video_data = {
                        'title': item['snippet']['title'],
                        'channel': item['snippet']['channelTitle'],
                        'views': views,
                        'likes': likes,
                        'comments': comments,
                        'engagement_rate': engagement_rate
                    }
                    all_videos.append(video_data)
                    
                    result += f"\n{video_data['title']}\n"
                    result += f"Channel: {video_data['channel']}\n"
                    result += f"Views: {video_data['views']:,}\n"
                    result += f"Engagement Rate: {video_data['engagement_rate']:.2f}%\n"
        
        # Analyze content gaps
        result += "\nContent Gap Analysis:\n"
        
        # Find high-performing topics
        high_engagement_threshold = sum(v['engagement_rate'] for v in all_videos) / len(all_videos)
        high_performing_videos = [v for v in all_videos if v['engagement_rate'] > high_engagement_threshold]
        
        # Extract common themes
        titles = [v['title'].lower() for v in high_performing_videos]
        common_themes = set()
        for title in titles:
            blob = TextBlob(title)
            common_themes.update([word for (word, tag) in blob.tags if tag.startswith('NN')])
        
        result += "\nPopular Content Themes:\n"
        for theme in common_themes:
            result += f"- {theme}\n"
        
        # Recommendations
        result += "\nRecommendations:\n"
        result += "1. Focus on high-engagement topics\n"
        result += f"2. Target engagement rates above {high_engagement_threshold:.2f}%\n"
        result += "3. Consider creating content around these themes:\n"
        for theme in list(common_themes)[:5]:
            result += f"   - {theme}\n"
        
        return result

if __name__ == "__main__":
    tool = CompetitorAnalyzer(
        keywords=["python programming tutorial", "coding tips"],
        max_results=5
    )
    print(tool.run()) 