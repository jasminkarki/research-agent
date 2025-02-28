# research-agent


### Smart Research Assistant: An Introduction
Smart Research Assistant is an AI-powered tool designed to revolutionize the research process by leveraging advanced natural language processing and machine learning techniques. This project aims to streamline literature discovery, data analysis, and insight generation for academics, professionals, and students.

### Problem Statement:
Researchers often struggle with the time-consuming tasks of literature review, data synthesis, and analysis, which can impede the progress of their work. This Smart Research Assistant addresses this challenge by automating these processes, allowing researchers to focus on interpretation and innovation.

### Data Flow:
1. User inputs a research topic or query
2. The system fetches relevant academic papers from databases like ArXiv
3. AI agents process the papers, generating summaries and extracting key insights
4. The system analyzes and synthesizes information across multiple papers
5. Results are presented to the user in a structured, easily digestible format

### Use Case:
A research scholar in computer science is researching advancements in natural language processing. They input their topic into the Smart Research Assistant, which then:
1. Retrieves 50+ relevant papers from academic databases
2. Generates concise summaries of each paper
3. Extracts key insights and identifies emerging trends in the field
4. Presents a comprehensive overview of the current state of NLP research
5. Suggests potential research directions based on gaps in the literature

This process, which might typically take weeks, is completed in a few minutes of the time, allowing the scholar to quickly gain a deep understanding of their research area and identify promising avenues for their own work.

### Installation Step
1. Clone the project repository:
   ```
   git clone https://github.com/your-username/Smart-Research-Assistant.git
   cd Smart-Research-Assistant
   ```

2. Create a virtual environment with Python 3.10+
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

7. Run the application:
   ```
   streamlit run src/main.py
   ```

8. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

9. Enter a research topic in the text input field and click "Research" to start the analysis process.

```
research-agent
│
├── src/                          # Source code for the application
│   ├── agents/                   # AI agents for different tasks
│   │   ├── __init__.py
│   │   ├── base_agent.py         # Base class for all agents
│   │   ├── summarizer_agent.py   # Agent for summarizing papers
│   │   ├── analyzer_agent.py     # Agent for analyzing content
│   │   ├── adv_dis_agent.py      # Agent for advantages/disadvantages
│   │   └── reference_linking_agent.py  # Agent for linking references
│   │
│   ├── data/                     # Data handling modules
│   │   ├── __init__.py
│   │   ├── data_loader.py        # Loads data from sources
│   │   └── real_time_fetcher.py  # Fetches real-time data
│   │
│   ├── utils/                    # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── config.py             # Configuration management
│   │   ├── logger.py             # Logging setup and functions
│   │   └── image_extractor.py    # Extracts images from PDFs
│   │
│   └── main.py                   # Main entry point of the application
│
├── tests/                        # Unit and integration tests
│   ├── __init__.py
│   ├── test_agents.py            # Tests for AI agents
│   └── test_data_loader.py       # Tests for data loading
│
├── notebooks/                    # Jupyter notebooks for analysis
│
├── config/                       # Configuration files
│   └── config.yaml               # YAML config for the project
│
├── requirements.txt              # Project dependencies
├── setup.py                      # Setup script for the project
├── pyproject.toml                # Project metadata and build system config
├── .env                          # Environment variables (git-ignored)
├── .gitignore                    # Specifies intentionally untracked files
└── README.md                     # Project documentation and overview
```

### Todo
- [✔️] Implement AI agent for summarization, pros/cons and few references 
- [⬜️] Integrate multiple data sources and more readable details to the result
- [⬜️] Optimize performance for large datasets
- [⬜️] Include better library for proper chain of agents
