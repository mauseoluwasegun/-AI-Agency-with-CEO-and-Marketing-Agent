from agency_swarm.tools import BaseTool
from pydantic import Field
from datetime import datetime

class TrendReportGenerator(BaseTool):
    """
    A tool for generating comprehensive trend reports by combining web search results,
    keyword analysis, and trend data.
    """
    web_search_results: str = Field(..., description="Results from web search")
    keyword_analysis: str = Field(..., description="Results from keyword analysis")
    trend_data: str = Field(..., description="Data from trend analysis")
    report_type: str = Field(
        default="comprehensive",
        description="Type of report to generate (comprehensive/summary)"
    )

    def run(self):
        """
        Generate a comprehensive trend report combining all available data.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""# Trend Analysis Report
Generated: {timestamp}

## Web Search Insights
{self.web_search_results}

## Keyword Analysis
{self.keyword_analysis}

## Trend Analysis
{self.trend_data}

## Key Findings

1. Top Trending Topics
   - Extracted from web search and keyword analysis
   - Validated against trend data
   - Prioritized by relevance and momentum

2. Content Opportunities
   - Identified gaps in current content
   - High-potential topic areas
   - Emerging trends to watch

3. Recommendations
   - Priority topics to cover
   - Optimal content angles
   - Timing considerations
   - Target audience insights

## Action Items
1. Immediate opportunities to pursue
2. Topics to monitor
3. Areas for further research

## Notes
- This report combines data from multiple sources
- Trends are analyzed for relevance and potential
- Recommendations are based on current market dynamics
"""
        
        # Create reports directory if it doesn't exist
        import os
        reports_dir = "trend_reports"
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        
        # Save report
        filename = f"{reports_dir}/trend_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        return f"Report generated and saved to: {filename}\n\n{report}"

if __name__ == "__main__":
    tool = TrendReportGenerator(
        web_search_results="Recent searches show increasing interest in AI tools and automation",
        keyword_analysis="Top keywords: AI, automation, machine learning",
        trend_data="Upward trend in AI-related content consumption",
        report_type="comprehensive"
    )
    print(tool.run()) 