from agency_swarm.tools import BaseTool
from pydantic import Field
from collections import Counter
import string
import re

class keyword_extractor(BaseTool):
    """
    A tool for extracting keywords from text content.
    It identifies important keywords and their frequencies.
    """
    text: str = Field(..., description="The text content to extract keywords from")
    max_keywords: int = Field(default=10, description="Maximum number of keywords to extract")
    min_word_length: int = Field(default=3, description="Minimum length for a word to be considered")

    def run(self):
        """
        Extract keywords from the provided text.
        """
        # Convert to lowercase
        text = self.text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        
        # Split into words
        words = text.split()
        
        # Remove common stop words
        stop_words = {
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
            'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
            'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her',
            'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there',
            'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get',
            'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no',
            'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your',
            'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then',
            'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also',
            'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first',
            'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these',
            'give', 'day', 'most', 'us', 'is', 'was', 'are', 'were', 'been',
            'has', 'had', 'did', 'doing', 'does', 'done'
        }
        
        # Filter words
        words = [word for word in words 
                if word not in stop_words 
                and len(word) >= self.min_word_length
                and not word.isnumeric()]
        
        # Count frequencies
        word_freq = Counter(words)
        
        # Get top keywords
        top_keywords = word_freq.most_common(self.max_keywords)
        
        # Format results
        result = "Extracted Keywords:\n\n"
        for word, freq in top_keywords:
            result += f"- {word}: {freq} occurrences\n"
            
        return result

if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence and Machine Learning are transforming the technology landscape.
    Companies are investing heavily in AI development and implementation.
    Deep learning models are becoming more sophisticated and efficient.
    """
    tool = keyword_extractor(text=sample_text, max_keywords=5)
    print(tool.run()) 