from agency_swarm import Agent

class TrendAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="Trend Analyzer",
            description="Responsible for analyzing current trends and market research using web search and trend analysis tools.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=4000
        ) 