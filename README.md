# YouTube Content Creation AI Agency 🎥

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Agency Swarm](https://img.shields.io/badge/Built%20with-Agency%20Swarm-orange)](https://github.com/VRSEN/agency-swarm)

An AI-powered agency that revolutionizes YouTube content creation using three specialized AI agents. Built with Agency Swarm and powered by Claude 3 Opus.

[Getting Started](#getting-started) • [Features](#features) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

## 🌟 Overview

This AI agency helps content creators:
- Generate trending content ideas backed by data
- Analyze channel performance and demographics
- Track competitor strategies and content gaps
- Create and manage content scripts
- Stay ahead of market trends

## 🤖 AI Agents

Three specialized agents work together seamlessly:

### Content Manager
- Generates creative content ideas using Claude 3 Opus
- Creates and edits scripts in markdown format
- Manages overall content strategy
- Coordinates insights from other agents

### Trend Analyzer
- Searches web trends using Tavily API
- Analyzes Google Trends data
- Extracts trending keywords
- Generates comprehensive trend reports

### YouTube Analyzer
- Analyzes channel metrics and demographics
- Tracks competitor performance
- Identifies content gaps and opportunities
- Evaluates audience engagement

## ⚡ Getting Started

### Prerequisites
- Python 3.8 or higher
- Required API keys:
  - OpenAI API key (agent communication)
  - Anthropic API key (content generation)
  - Tavily API key (web search)
  - YouTube Data API key (analytics)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-content-ai-agency.git
cd youtube-content-ai-agency
```

2. Install dependencies:
```bash
pip install -r content_creation_agency/requirements.txt
```

3. Set up environment variables in `.env`:
```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
TAVILY_API_KEY=your_tavily_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

4. Run the agency:
```bash
python content_creation_agency/agency.py
```

## 🎯 Features

### Content Strategy
- **AI-Powered Ideation**: Generate content ideas using Claude 3 Opus
- **Data-Driven Decisions**: Ideas backed by trend analysis and performance data
- **Script Management**: Write and version control your content scripts

### Analytics & Research
- **Channel Analytics**: Track performance, engagement, and demographics
- **Competitor Analysis**: Monitor strategies and identify opportunities
- **Trend Tracking**: Stay updated with latest industry trends

### Automation & Reports
- **Automated Research**: AI-powered web and trend analysis
- **Performance Reports**: Detailed analytics and insights
- **Content Gap Analysis**: Identify underserved topics and opportunities

## 🛠️ Technical Details

### Project Structure
```
content_creation_agency/
├── agency.py                 # Main agency file
├── agency_manifesto.md       # Agency's shared instructions
├── requirements.txt          # Project dependencies
├── content_manager/         # Content Manager agent
├── trend_analyzer/          # Trend Analyzer agent
└── youtube_analyzer/        # YouTube Analyzer agent
```

### Tools & APIs Used
- Agency Swarm Framework
- Claude 3 Opus (Anthropic)
- Tavily Search API
- YouTube Data API
- Google Trends API

## 📖 Documentation

- [Setup Guide](../../wiki/Setup-Guide)
- [API Reference](../../wiki/API-Reference)
- [Usage Examples](../../wiki/Usage-Examples)
- [Best Practices](../../wiki/Best-Practices)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Credits

Built with these amazing technologies:
- [Agency Swarm](https://github.com/VRSEN/agency-swarm) - Multi-agent framework
- [Claude 3 Opus](https://www.anthropic.com/claude) - Advanced language model
- [Tavily API](https://tavily.com) - Semantic search
- [YouTube Data API](https://developers.google.com/youtube/v3) - YouTube analytics

## 📧 Contact

For questions and support, please:
- Open an issue
- Contact us at irokomause@gmail.com
- Join our [Discord community](your-discord-link)

---
<div align="center">
Made with ❤️ bY mause
</div>
