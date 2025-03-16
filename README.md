# PDF Question-Answering System

A sophisticated system for processing PDF documents and answering queries using advanced NLP techniques and vector embeddings.

## Features

- PDF and text document processing
- Vector embedding generation for efficient search
- Interactive Q&A through a Streamlit interface
- Fast similarity search for context retrieval
- Comprehensive logging and error handling

## System Architecture

Please refer to [architecture.md](architecture.md) for detailed system documentation.

### Component Diagrams

The system consists of several key components working together:

1. Data Ingestion Pipeline
2. Embedding Generation System
3. Model API Service
4. Streamlit Web Interface

Visual representations of these components can be found in the diagrams folder:

### Data Ingestion Flow ((diagrams/data_ingestion.svg))
The data ingestion flowchart illustrates how the system processes incoming documents:
- Accepts PDF/Text input from users
- Processes documents through the ingestion pipeline
- Performs text chunking for optimal processing
- Stores raw data and generates processed text output
- Prepares data for the embedding generation phase

### Embedding System Flow ((diagrams/embedding.svg))
The embedding system flowchart shows the vector generation process:
- Takes processed text as input
- Generates vector embeddings using advanced NLP models
- Creates and manages vector store entries
- Builds search indices for fast retrieval
- Optimizes storage for quick access during query time

### Model API Flow (diagrams/model_api.svg))
The Model API flowchart demonstrates the query processing pipeline:
- Processes incoming user queries
- Performs vector similarity search
- Generates query embeddings
- Retrieves relevant context from stored data
- Generates final responses using the language model

### Web Interface Flow (](diagrams/streamlit_app.svg))
The Streamlit interface flowchart shows the user interaction flow:
- Provides file upload functionality
- Handles user query inputs
- Manages data processing requests
- Coordinates query processing
- Displays responses and results to users

### Complete System Architecture ((diagrams/system_architecture.svg))
The system architecture diagram provides a comprehensive view of how all components interact:
- Shows the complete data flow from input to response
- Illustrates component interactions and dependencies
- Demonstrates the system's modular design
- Highlights key integration points between components
- Provides a high-level overview of the entire system

## Project Structure

```
.
├── QA_WithPDF/
│   ├── data_ingestion.py    # Document processing and chunking
│   ├── embedding.py         # Vector embedding generation
│   └── model_api.py         # Query processing and response generation
├── StreamlitApp.py          # Web interface
├── storage/                 # Vector and index storage
├── logs/                    # System logs
├── diagrams/               # Architecture diagrams
└── notebook/               # Development notebooks
```

## Installation

1. Clone the repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run StreamlitApp.py
```

2. Upload a PDF document through the web interface
3. Ask questions about the document content
4. View generated responses based on document context

## Configuration

The system can be configured through environment variables or configuration files. Key settings include:

- Chunking parameters
- Embedding model selection
- Vector store configuration
- API settings

## Error Handling

The system includes comprehensive error handling and logging:

- Detailed logs in the `logs/` directory
- Exception handling for various failure scenarios
- User-friendly error messages in the interface

## Development

For development and testing:

1. Check the `notebook/` directory for development notebooks
2. Use the logger for debugging
3. Refer to architecture documentation for system design

## Dependencies

Key dependencies include:

- Streamlit for web interface
- LangChain for embeddings
- PyPDF2 for PDF processing
- FAISS for vector storage

For a complete list, see `requirements.txt`.
