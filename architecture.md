# System Architecture

## Overview
This QA system is designed to process PDF documents and text inputs, generate embeddings, and provide relevant answers to user queries using a sophisticated question-answering pipeline.

## Core Components

### 1. Data Ingestion (data_ingestion.py)
- Handles input processing of PDF documents and text files
- Performs text chunking for efficient processing
- Manages raw data storage and initial text processing
- Prepares data for embedding generation

### 2. Embedding Generation (embedding.py)
- Converts processed text into vector embeddings
- Manages vector store operations
- Creates and maintains index for fast similarity search
- Optimizes storage of embeddings for quick retrieval

### 3. Model API (model_api.py)
- Processes user queries
- Performs vector similarity search
- Retrieves relevant context from stored embeddings
- Generates responses using the language model
- Handles query embedding and context integration

### 4. Web Interface (StreamlitApp.py)
- Provides user-friendly interface using Streamlit
- Manages file upload functionality
- Handles user query input
- Displays responses and results
- Coordinates between frontend and backend components

## Data Flow
1. User uploads documents through the web interface
2. Data ingestion component processes and chunks the documents
3. Embedding generation creates vector representations
4. Vector store indexes and stores embeddings
5. User submits queries through the interface
6. Model API processes queries and retrieves relevant context
7. System generates and displays responses

## Storage
- Vector Store: Manages document embeddings
- Index Store: Maintains search indices
- Raw Data Storage: Stores original document chunks

## Integration Points
- Web Interface ↔ Data Ingestion: File upload and processing
- Data Ingestion ↔ Embedding: Text processing pipeline
- Embedding ↔ Storage: Vector and index management
- Model API ↔ Storage: Context retrieval
- Model API ↔ Web Interface: Query processing and response display

## Error Handling
- Logging system for tracking operations
- Exception handling for various failure scenarios
- Graceful degradation when components fail

## Configuration
- Environment variables for model settings
- Configurable chunking and embedding parameters
- Adjustable vector store settings

Please refer to the diagrams folder for visual representations of the architecture.
