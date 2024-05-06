""" 
Basic example of scraping pipeline using SmartScraper using Azure OpenAI Key
"""

import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings


# required environment variables in .env
# HUGGINGFACEHUB_API_TOKEN
# ANTHROPIC_API_KEY
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# ************************************************
# Initialize the model instances
# ************************************************


embedder_model_instance = HuggingFaceInferenceAPIEmbeddings(
    api_key=HUGGINGFACEHUB_API_TOKEN, model_name="sentence-transformers/all-MiniLM-l6-v2"
)

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

graph_config = {
    "llm": {
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "model": "claude-3-haiku-20240307",
        "max_tokens": 4000},
    "embeddings": {"model_instance": embedder_model_instance}
}

smart_scraper_graph = SmartScraperGraph(
    prompt="""Don't say anything else. Output JSON only. List me all the events, with the following fields: company_name, event_name, event_start_date, event_start_time, 
    event_end_date, event_end_time, location, event_mode, event_category, 
    third_party_redirect, no_of_days, 
    time_in_hours, hosted_or_attending, refreshments_type, 
    registration_available, registration_link""",
    # also accepts a string with the already downloaded HTML code
    source="https://www.hmhco.com/event",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))
