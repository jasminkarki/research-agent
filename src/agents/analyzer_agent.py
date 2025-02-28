from .base_agent import BaseAgent

class AnalyzerAgent(BaseAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="analyzer_agent",
            system_message="Analyze research papers and provide key insights in a structured, bullet-point format.",
            llm_config=llm_config
        )

    def analyze(self, paper_summary):
        response = self.generate_reply([{"role": "user", "content": f"Analyze this summary and provide 3-5 key insights in bullet-point format:\n\n{paper_summary}"}])
        return response['content'] if isinstance(response, dict) else response
