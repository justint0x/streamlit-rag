# RAG Application using Streamlit and Langchain

This project is a Retrieval-Augmented Generation (RAG) application built using Streamlit and Langchain. The application allows users to retrieve information from various document formats including PDF, DOC, XLS, and TXT files.

## Project Structure

```
my-rag-app
├── app.py                # Main entry point of the Streamlit application
├── data                  # Directory containing sample data files
│   ├── sample.pdf        # Sample PDF file for testing
│   ├── sample.doc        # Sample DOC file for testing
│   ├── sample.xls        # Sample XLS file for testing
│   └── sample.txt        # Sample TXT file for testing
├── requirements.txt      # List of dependencies for the project
├── utils                 # Directory containing utility functions
│   └── retriever.py      # Functions for retrieving content from files
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-rag-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Application Functionality

- The application allows users to upload documents in PDF, DOC, XLS, and TXT formats.
- It utilizes Langchain for processing and retrieving relevant information from the uploaded documents.
- Users can input queries and receive generated responses based on the content of the documents.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.