from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.azuresearch import AzureSearch
import os
import logging


service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

def upload_document(receivved_data: dict):
    # [START upload_document]
    DOCUMENT = receivved_data
    
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        chunk_size=1,
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        show_progress_bar=True
    )
    
    azure_ai_search = AzureSearch(
        azure_search_endpoint=os.getenv('AZURE_SEARCH_SERVICE_ENDPOINT'),
        azure_search_key=os.getenv('AZURE_SEARCH_API_KEY'),
        index_name=os.getenv('AZURE_SEARCH_INDEX_NAME'),
        embedding_function=embeddings.embed_query
    )

    azure_ai_search.add_texts(texts=DOCUMENT)

    print("\n\nUpload of new document succeeded!!\n\n")
    # [END upload_document]