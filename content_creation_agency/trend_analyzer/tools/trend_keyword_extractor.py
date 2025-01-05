from agency_swarm.tools import BaseTool
from pydantic import Field
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from collections import Counter
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

class TrendKeywordExtractor(BaseTool):
    """
    A tool for extracting trending keywords from search results and articles.
    It identifies important keywords and their frequencies from trend data.
    """
    search_results: str = Field(..., description="The search results text to extract keywords from")
    max_keywords: int = Field(default=15, description="Maximum number of keywords to extract")
    min_frequency: int = Field(default=2, description="Minimum frequency for a keyword to be considered trending")

    def run(self):
        """
        Extract trending keywords from the provided search results.
        """
        # Tokenize and convert to lowercase
        tokens = word_tokenize(self.search_results.lower())
        
        # Remove punctuation and stopwords
        stop_words = set(stopwords.words('english'))
        custom_stop_words = {'latest', 'trending', 'trend', 'new', 'update', 'updates', 'video', 'videos'}
        stop_words.update(custom_stop_words)
        
        tokens = [word for word in tokens 
                 if word not in string.punctuation 
                 and word not in stop_words
                 and len(word) > 2]
        
        # Get POS tags
        pos_tags = pos_tag(tokens)
        
        # Keep only nouns, adjectives, and verbs
        important_words = [word for word, tag in pos_tags 
                         if tag.startswith(('NN', 'JJ', 'VB'))]
        
        # Count frequencies
        word_freq = Counter(important_words)
        
        # Filter by minimum frequency
        trending_keywords = {word: freq for word, freq in word_freq.items() 
                           if freq >= self.min_frequency}
        
        # Get top keywords
        top_keywords = Counter(trending_keywords).most_common(self.max_keywords)
        
        # Format results
        result = "Trending Keywords Analysis:\n\n"
        
        if not top_keywords:
            return "No trending keywords found with the specified minimum frequency."
        
        # Group by frequency
        freq_groups = {}
        for word, freq in top_keywords:
            if freq not in freq_groups:
                freq_groups[freq] = []
            freq_groups[freq].append(word)
        
        # Output grouped by frequency
        for freq in sorted(freq_groups.keys(), reverse=True):
            result += f"\nMentioned {freq} times:\n"
            for word in sorted(freq_groups[freq]):
                result += f"- {word}\n"
            
        return result

if __name__ == "__main__":
    sample_text = """
    The latest trends in content creation show a surge in AI-powered tools and automation.
    Content creators are increasingly focusing on AI tutorials and productivity tools.
    Machine learning applications are becoming more accessible to beginners.
    Several trending topics include artificial intelligence, automation tools, and coding tutorials.
    """
    tool = TrendKeywordExtractor(search_results=sample_text, max_keywords=10, min_frequency=2)
    print(tool.run()) 