from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from datetime import datetime, timedelta

load_dotenv()

class ChannelAnalyzer(BaseTool):
    """
    A tool for analyzing YouTube channel performance and demographics.
    It can analyze channel statistics, video performance, and audience demographics.
    """
    channel_id: str = Field(..., description="The YouTube channel ID to analyze")
    days_to_analyze: int = Field(default=30, description="Number of days of data to analyze")

    def run(self):
        """
        Analyze YouTube channel performance and demographics.
        """
        youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
        
        # Get channel statistics
        channel_response = youtube.channels().list(
            part='snippet,statistics,contentDetails',
            id=self.channel_id
        ).execute()
        
        if not channel_response['items']:
            return "Channel not found"
            
        channel = channel_response['items'][0]
        
        # Get channel's uploads playlist
        uploads_playlist_id = channel['contentDetails']['relatedPlaylists']['uploads']
        
        # Get recent videos
        videos_response = youtube.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=uploads_playlist_id,
            maxResults=50
        ).execute()
        
        # Format results
        result = "Channel Analysis Report\n\n"
        
        # Channel overview
        result += "Channel Overview:\n"
        result += f"- Name: {channel['snippet']['title']}\n"
        result += f"- Subscribers: {channel['statistics']['subscriberCount']}\n"
        result += f"- Total Views: {channel['statistics']['viewCount']}\n"
        result += f"- Total Videos: {channel['statistics']['videoCount']}\n"
        
        # Recent videos analysis
        result += "\nRecent Videos Performance:\n"
        for item in videos_response.get('items', [])[:5]:
            video_id = item['contentDetails']['videoId']
            video_stats = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()
            
            if video_stats['items']:
                stats = video_stats['items'][0]['statistics']
                result += f"\n{item['snippet']['title']}\n"
                result += f"- Views: {stats.get('viewCount', 'N/A')}\n"
                result += f"- Likes: {stats.get('likeCount', 'N/A')}\n"
                result += f"- Comments: {stats.get('commentCount', 'N/A')}\n"
        
        return result

if __name__ == "__main__":
    tool = ChannelAnalyzer(
        channel_id="UCTOfY0ASxDZ1gsSe2s5GBQA",
        days_to_analyze=30
    )
    print(tool.run()) 