from .base_agent import BaseAgent

class AdvDisAgent(BaseAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="adv_dis_agent",
            system_message="Analyze research papers and provide advantages and disadvantages in a structured format.",
            llm_config=llm_config
        )

    def get_adv_dis(self, paper_summary):
        response = self.generate_reply([{"role": "user", "content": f"Based on this summary, list 2-3 advantages and 2-3 disadvantages of the research:\n\n{paper_summary}"}])
        return response['content'] if isinstance(response, dict) else response
