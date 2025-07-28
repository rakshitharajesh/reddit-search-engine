from exa_py import Exa
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
exa = Exa(api_key)
query = input("search here:")

result = exa.search(
    query,
    num_results = 3,
    start_publshed_date = "2025-01-01",
    type = "neural",
    include_domains = ['https://www.reddit.com/']
)

for result in response.results:
    print(f"Title: {result.title}")
    print(f"URL: {result.url}")
    print(f"Published Date: {result.published_date}")