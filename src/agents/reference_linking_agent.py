from .base_agent import BaseAgent

class ReferenceLinkingAgent(BaseAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="reference_linking_agent",
            system_message="Extract and link references from research papers.",
            llm_config=llm_config
        )

    def extract_references(self, paper_content):
        response = self.generate_reply([{"role": "user", "content": f"Extract and format the references from this paper content:\n\n{paper_content}"}])
        return response['content'] if isinstance(response, dict) else response

    def link_references(self, references, query):
        response = self.generate_reply([{"role": "user", "content": f"Link these references to the query '{query}':\n\n{references}"}])
        return response['content'] if isinstance(response, dict) else response
