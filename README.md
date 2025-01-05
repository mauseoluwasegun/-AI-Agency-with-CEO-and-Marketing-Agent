# AI-Powered Content Creation Agency with YouTube Analytics

An intelligent content creation agency built with Agency Swarm framework, leveraging multiple AI agents to optimize content strategy and YouTube channel performance.

## 🤖 Agents Overview

### 1. Content Manager
- Generates creative content ideas using Claude 3 Opus
- Creates and edits scripts in markdown format
- Manages overall content strategy
- Coordinates with other agents for insights

### 2. Trend Analyzer
- Searches web trends using Tavily API
- Analyzes Google Trends data
- Extracts trending keywords
- Generates comprehensive trend reports

### 3. YouTube Analyzer
- Analyzes channel performance metrics
- Tracks audience demographics
- Monitors competitor strategies
- Identifies content gaps and opportunities

## 🚀 Features

- **Data-Driven Content Ideation**: Generate content ideas based on market trends and performance data
- **Automated Trend Analysis**: Stay updated with the latest trends in your niche
- **YouTube Analytics**: Track channel performance, audience engagement, and competitor strategies
- **Script Management**: Write and edit scripts with automatic versioning
- **Collaborative AI Workflow**: Agents work together to optimize content strategy
- **Comprehensive Reporting**: Generate detailed reports on trends and performance

## 📋 Prerequisites

- Python 3.8 or higher
- Required API keys:
  - OpenAI API key (for agent communication)
  - Anthropic API key (for content generation)
  - Tavily API key (for web search)
  - YouTube Data API key (for YouTube analytics)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-content-creation-agency.git
cd ai-content-creation-agency
```

2. Install dependencies:
```bash
pip install -r content_creation_agency/requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
TAVILY_API_KEY=your_tavily_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

## 🎯 Usage

1. Run the agency:
```bash
python content_creation_agency/agency.py
```

2. The agency will:
   - Analyze latest YouTube video performance
   - Analyze current trends
   - Generate content ideas
   - Get user confirmation
   - Write and edit scripts

## 📁 Project Structure

```
content_creation_agency/
├── agency.py                 # Main agency file
├── agency_manifesto.md       # Agency's shared instructions
├── requirements.txt          # Project dependencies
├── content_manager/         # Content Manager agent
│   ├── content_manager.py
│   ├── instructions.md
│   └── tools/
│       ├── content_generator.py
│       ├── keyword_extractor.py
│       └── script_writer.py
├── trend_analyzer/          # Trend Analyzer agent
│   ├── trend_analyzer.py
│   ├── instructions.md
│   └── tools/
│       ├── web_searcher.py
│       ├── trend_analyzer.py
│       └── trend_report_generator.py
└── youtube_analyzer/        # YouTube Analyzer agent
    ├── youtube_analyzer.py
    ├── instructions.md
    └── tools/
        ├── channel_analyzer.py
        └── competitor_analyzer.py
```

## 🛠️ Tools Overview

### Content Manager Tools
- `content_generator.py`: Generates content ideas using Claude 3 Opus
- `keyword_extractor.py`: Extracts and analyzes keywords from text
- `script_writer.py`: Creates and manages script files

### Trend Analyzer Tools
- `web_searcher.py`: Searches web using Tavily API
- `trend_analyzer.py`: Analyzes Google Trends data
- `trend_report_generator.py`: Creates comprehensive trend reports

### YouTube Analyzer Tools
- `channel_analyzer.py`: Analyzes channel performance
- `competitor_analyzer.py`: Analyzes competitor channels

## 📊 Generated Files

The agency creates several types of files:
- Script drafts in `scripts/` directory
- Trend reports in `trend_reports/` directory
- Performance analysis reports

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Agency Swarm Framework](https://github.com/VRSEN/agency-swarm)
- Anthropic's Claude API
- Tavily Search API
- YouTube Data API
- Google Trends API 