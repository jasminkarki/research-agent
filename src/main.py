import streamlit as st
from agents.summarizer_agent import SummarizerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.adv_dis_agent import AdvDisAgent
from agents.reference_linking_agent import ReferenceLinkingAgent
from agents.task_manager import TaskManager
from data.data_loader import DataLoader
from data.real_time_fetcher import RealTimeFetcher
from utils.config import load_config
from utils.logger import setup_logger
from utils.image_extractor import extract_images_from_pdf

logger = setup_logger('main')

def main():
    config = load_config()
    
    st.title("An Advanced Research Assistant at your service")

    llm_config = {'config_list': [{'model': config['model_name'], 'api_key': config['groq_api_key'], 'api_type': "groq"}]}
    
    summarizer = SummarizerAgent(llm_config)
    analyzer = AnalyzerAgent(llm_config)
    adv_dis_agent = AdvDisAgent(llm_config)
    ref_linking_agent = ReferenceLinkingAgent(llm_config)
    task_manager = TaskManager(summarizer, analyzer, adv_dis_agent, ref_linking_agent)
    data_loader = DataLoader()
    real_time_fetcher = RealTimeFetcher(config['news_api_key'])

    query = st.text_input("Enter a research topic:")
    if st.button("Research"):
        with st.spinner("Researching..."):
            logger.info(f"Starting research on topic: {query}")
            
            logger.info("Fetching papers from ArXiv")
            papers = data_loader.fetch_arxiv_papers(query)
            logger.info(f"Fetched {len(papers)} papers from ArXiv")
            
            logger.info("Fetching news articles")
            news = real_time_fetcher.fetch_news_articles(query)
            logger.info(f"Fetched {len(news)} news articles")
            
            logger.info("Processing papers")
            results = task_manager.batch_process(papers, query)
            logger.info("Finished processing papers")
            
            st.subheader("Research Papers")
            for paper, result in zip(papers, results):
                st.write(f"**{paper['title']}**")
                st.write("**Summary:**")
                st.write(result['summary'])
                st.write("**Key Insights:**")
                st.write(result['analysis'])
                st.write("**Advantages and Disadvantages:**")
                st.write(result['adv_dis'])
                
                # # Display important diagrams
                # images = extract_images_from_pdf(paper['pdf_url'])
                # if images:
                #     st.write("**Important Diagrams:**")
                #     for img in images[:3]:  # Display up to 3 images
                #         st.image(img, use_column_width=True)
                
                st.write("**Linked References:**")
                st.write(result['linked_refs'])
                
                st.write(f"[Read full paper]({paper['link']})")
                st.write("---")
            
            st.subheader("Related News")
            for article in news:
                st.write(f"**{article['title']}**")
                st.write(article['description'])
                st.write(f"[Read more]({article['url']})")
                st.write("---")
            
            logger.info("Research complete")


if __name__ == "__main__":
    main()
