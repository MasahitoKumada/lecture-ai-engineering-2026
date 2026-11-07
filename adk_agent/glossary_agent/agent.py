from google.adk.agents import Agent

from app import tools
from app.agent import INSTRUCTIONS

root_agent = Agent(
    name="glossary_agent",
    description="AIE2026 の用語と講義要点を調べて、学習支援として説明するエージェント",
    model="gemini-3.5-flash-lite",
    instruction=INSTRUCTIONS,
    tools=[
        tools.search_glossary,
        tools.get_lecture_summary,
    ],
)
