import os
from llama_index.core import VectorStoreIndex
# Configure global settings
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini


from QA_WithPDF.data_ingestion import load_data
from QA_WithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

google_api_key = os.getenv('GOOGLE_API_KEY')

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        
        # Initialize LLM and embedding models
        
        embed_model  = GeminiEmbedding(model_name="models/embedding-001")
        Settings.embed_model = embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
        Settings.llm = model
        
        logging.info("")
        index = VectorStoreIndex.from_documents(document, embed_model=embed_model)
        index.storage_context.persist()
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)