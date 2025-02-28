from utils.image_extractor import extract_images_from_pdf

class TaskManager:
    def __init__(self, summarizer, analyzer, adv_dis_agent, ref_linking_agent):
        self.summarizer = summarizer
        self.analyzer = analyzer
        self.adv_dis_agent = adv_dis_agent
        self.ref_linking_agent = ref_linking_agent

    def process_paper(self, paper_content, query):
        summary = self.summarizer.summarize(paper_content)
        analysis = self.analyzer.analyze(summary)
        adv_dis = self.adv_dis_agent.get_adv_dis(summary)
        references = self.ref_linking_agent.extract_references(paper_content)
        linked_refs = self.ref_linking_agent.link_references(references, query)
        # images = extract_images_from_pdf(paper['pdf_url'])

        return {
            "summary": summary,
            "analysis": analysis,
            "adv_dis": adv_dis,
            "references": references,
            "linked_refs": linked_refs,
            # "images": images
        }
    
    def batch_process(self, papers, query):
        return [self.process_paper(paper, query) for paper in papers]

