# Product Information Chatbot

## Overview
The Product Information Chatbot is an interactive application that allows users to upload product PDF documents and ask questions about those products. The chatbot leverages natural language processing and document retrieval techniques to provide accurate, relevant answers based on the content of the uploaded documents.

## Features
- PDF document upload functionality
- Natural language query processing
- Context-aware responses using advanced language models
- User-friendly interface built with Streamlit
- Fast document retrieval using FAISS vector storage

## Technology Stack
- **Frontend**: Streamlit
- **Language Model**: LLaMA 3 (8B parameters) via Groq API
- **Embeddings**: Hugging Face's sentence-transformers/all-MiniLM-L6-v2
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Document Processing**: LangChain's PDF loader and text splitter

## How It Works
1. The user uploads a PDF containing product information
2. The application processes the PDF document:
   - Extracts the text content
   - Splits it into manageable chunks
   - Creates vector embeddings for semantic search
3. The user asks questions in natural language about the products
4. The system:
   - Retrieves relevant document sections based on the query
   - Passes the context and query to the language model
   - Returns a concise, informative answer based on the product documentation

## Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (for accessing the LLaMA 3 model)

### Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/product-information-chatbot.git
cd product-information-chatbot
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your Groq API key
```
GROQ_API_KEY=your_groq_api_key
```

## Usage
1. Run the Streamlit application
```bash
streamlit run app.py
```

2. Access the application through your web browser (typically at http://localhost:8501)

3. Upload a product PDF document

4. Ask questions about the products in the document

## Example Questions
- "What are the technical specifications of product X?"
- "Does this product come with a warranty?"
- "What colors is this item available in?"
- "How much does this product cost?"
- "What are the shipping options for this product?"


```

## Future Enhancements
- Support for additional document formats (DOCX, HTML, etc.)
- Multi-document querying capability
- Answer summarization for lengthy responses
- Product comparison functionality
- User feedback collection to improve responses
- Integration with product databases and APIs

## License
MIT License

## Contributors
Faisel Ahmad
