# Import necessary libraries
import os
from dotenv import load_dotenv
import httpx
from langchain_community.llms import VLLMOpenAI

# Load environment variables from .env file
load_dotenv()

# Get Granite model information from environment variables
granite_model_name = os.getenv('GRANITE_MODEL_NAME')
granite_api_url = os.getenv('GRANITE_API_URL')
granite_api_key = os.getenv('GRANITE_API_KEY')

# Initialize VLLMOpenAI for Granite
granite_llm = VLLMOpenAI(
    openai_api_key=granite_api_key,
    openai_api_base=granite_api_url,
    model_name=granite_model_name,
    temperature=0,
    verbose=False,
    streaming=False,
    max_tokens=5000,
    async_client=httpx.AsyncClient(verify=False),
    http_client=httpx.Client(verify=False)
)

# Test the Granite LLM with a simple prompt
test_prompt = "Show me sample ansible code"

try:
    # Use invoke method instead of __call__
    response = granite_llm.invoke(test_prompt)
    print(f"Granite LLM Response: {response}")
except Exception as e:
    print(f"An error occurred: {e}")
