from langchain.serpapi import SerpAPIWrapper
from decouple import config


def get_information(text: str) -> str:
    search = SerpAPIWrapper(serpapi_api_key=config("SERPAPI_API_KEY"))
    res = search.run(f"{text}")

    return res
