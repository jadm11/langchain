# LangChain Q&A System

A question-answering system built with LangChain and ChromaDB that provides accurate answers based on a knowledge base.

## Features

- Document loading and text splitting
- Vector embeddings using OpenAI
- Persistent vector storage with ChromaDB
- Interactive question-answering interface
- Cross-platform compatibility

## Project Structure

```
project/
├── data/                  # Knowledge base files
│   └── knowledge.txt
├── db/                    # Vector database storage
│   └── chroma_db/
├── src/                   # Source code
│   └── qa_system.py
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key with sufficient credits
- Required Python packages:
  - langchain>=0.1.0
  - openai>=1.0.0
  - chromadb>=0.4.0

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. Add your knowledge base file to the `data/` directory:
   - Place your text file in `data/knowledge.txt`
   - The system will automatically split and process the content

## Knowledge Base

The system comes with a pre-configured knowledge base about migratory birds in `data/knowledge.txt`. You can:
- Replace the content with your own knowledge base
- Ensure the text is well-structured with clear headings and sections
- Keep the file size reasonable for optimal performance

## Usage

1. Run the Q&A system:
   ```bash
   python src/qa_system.py
   ```

2. Enter your questions when prompted
3. Type 'quit' to exit the program

## Example Questions

The system is optimized for questions about:
- Basic migration concepts and navigation methods
- Different types of migration (Latitudinal, Longitudinal, Altitudinal)
- Notable migratory species and their records
- Conservation challenges and efforts
- Migration timing and seasons

## How It Works

1. The system loads your knowledge base from `data/knowledge.txt`
2. Documents are split into chunks for processing
3. OpenAI embeddings are generated for each chunk
4. ChromaDB stores the embeddings persistently
5. When you ask a question:
   - The question is embedded
   - Similar chunks are retrieved
   - An answer is generated using the context

## Maintenance

- The vector database is stored in `db/chroma_db/`
- To force a fresh start, delete the `db/chroma_db/` directory
- The system will automatically recreate the database on next run

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security Setup

1. Create a `.env` file in the project root
2. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
3. Ensure `.env` is listed in your `.gitignore`
4. Never commit the `.env` file or share it publicly

## API Usage and Limits

- Maximum query length: 500 characters
- Rate limits: Follow OpenAI's API rate limits
- Error handling: The system provides clear error messages without exposing sensitive information

## Error Recovery

If you encounter errors:
1. Check your API key is valid
2. Ensure the knowledge.txt file exists
3. Verify you have sufficient API credits
4. Check your internet connection

## Version

Current version: 1.0.0 