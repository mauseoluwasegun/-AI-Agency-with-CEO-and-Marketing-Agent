from agency_swarm.tools import BaseTool
from pydantic import Field
import os
from datetime import datetime

class ScriptWriter(BaseTool):
    """
    A tool for writing and editing video scripts in markdown format.
    Scripts are saved locally with timestamps.
    """
    title: str = Field(..., description="Title of the video")
    content: str = Field(..., description="Content of the script in markdown format")
    script_type: str = Field(default="draft", description="Type of script (draft/final)")
    
    def run(self):
        """
        Write or edit a script and save it locally.
        """
        # Create scripts directory if it doesn't exist
        scripts_dir = "scripts"
        if not os.path.exists(scripts_dir):
            os.makedirs(scripts_dir)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{scripts_dir}/{self.title.replace(' ', '_')}_{self.script_type}_{timestamp}.md"
        
        # Add metadata header to the content
        script_content = f"""---
title: {self.title}
type: {self.script_type}
created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---

{self.content}
"""
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        return f"Script saved successfully to: {filename}"

if __name__ == "__main__":
    tool = ScriptWriter(
        title="Test Video",
        content="""# Introduction
        
Hello everyone! Welcome to this test video.

## Main Points

1. First point
2. Second point
3. Third point

## Conclusion

Thanks for watching!
""",
        script_type="draft"
    )
    print(tool.run()) 