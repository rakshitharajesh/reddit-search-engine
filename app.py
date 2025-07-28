import os
from dotenv import load_dotenv
import streamlit as st
from exa_py import Exa

load_dotenv()
api_key = os.getenv("API_KEY")
exa = Exa(api_key)

st.title("Reddit Search Engine")
query = st.text_input("Enter your search query here: ")
search_btn = st.button("Search")

if search_btn and query:
    with st.spinner("Searching..."):
        try:
            response = exa.search(
                query,
                num_results=3,
                start_published_date="2025-01-01",
                type="keyword",
                include_domains=["https://www.reddit.com/"]
            )
            if response.results:
                for result in response.results:
                    st.subheader(result.title)
                    st.write(f"URL: {result.url}")
                    st.write(f"Published Date: {result.published_date}")
                    st.markdown("---")
            else:
                st.warning("No results found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

