from agency_swarm import Agent

class YouTubeAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            name="YouTube Analyzer",
            description="Responsible for analyzing YouTube channel performance, audience demographics, and competitor analysis.",
            instructions="./instructions.md",
            tools_folder="./tools",
            temperature=0.5,
            max_prompt_tokens=4000
        ) 