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

class KeywordExtractor(BaseTool):
    """
    A tool for extracting keywords from text content using NLTK.
    It identifies important keywords and their frequencies.
    """
    text: str = Field(..., description="The text content to extract keywords from")
    max_keywords: int = Field(default=10, description="Maximum number of keywords to extract")

    def run(self):
        """
        Extract keywords from the provided text using NLTK.
        """
        # Tokenize and convert to lowercase
        tokens = word_tokenize(self.text.lower())
        
        # Remove punctuation and stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens 
                 if word not in string.punctuation 
                 and word not in stop_words
                 and len(word) > 2]
        
        # Get POS tags
        pos_tags = pos_tag(tokens)
        
        # Keep only nouns and adjectives
        important_words = [word for word, tag in pos_tags 
                         if tag.startswith(('NN', 'JJ'))]
        
        # Count frequencies
        word_freq = Counter(important_words)
        
        # Get top keywords
        top_keywords = word_freq.most_common(self.max_keywords)
        
        # Format results
        result = "Extracted Keywords:\n"
        for word, freq in top_keywords:
            result += f"- {word}: {freq} occurrences\n"
            
        return result

if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence and Machine Learning are transforming the technology landscape.
    Companies are investing heavily in AI development and implementation.
    Deep learning models are becoming more sophisticated and efficient.
    """
    tool = KeywordExtractor(text=sample_text, max_keywords=5)
    print(tool.run()) 