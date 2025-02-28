from .base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="summarizer_agent",
            system_message="Summarize research papers concisely in a clear, readable format.",
            llm_config=llm_config
        )

    def summarize(self, paper_content):
        response = self.generate_reply([{"role": "user", "content": f"Provide a clear, concise summary of this paper in about 3-4 sentences: {paper_content}"}])
        return response['content'] if isinstance(response, dict) else response
