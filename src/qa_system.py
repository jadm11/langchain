# Import required libraries for document loading, embeddings, and vector storage
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file (requires OPENAI_API_KEY)
load_dotenv()

def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent

def setup_qa_chain():
    """Initialize and configure the Q&A chain with document loading and vector storage.
    
    Returns:
        RetrievalQA: Configured Q&A chain ready for queries.
        
    Raises:
        ValueError: If OPENAI_API_KEY is not set
        FileNotFoundError: If knowledge.txt is not found
    """
    try:
        # Validate OpenAI API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        # Add basic API key format validation
        if not api_key.startswith("sk-") or len(api_key) < 20:
            raise ValueError("OPENAI_API_KEY appears to be malformed")

        # Set up directory structure for data and vector database
        project_root = get_project_root()
        data_dir = project_root / "data"
        db_dir = project_root / "db" / "chroma_db"
        
        # Create directories if they don't exist
        data_dir.mkdir(exist_ok=True)
        db_dir.mkdir(exist_ok=True)

        # Load knowledge base from text file
        knowledge_file = data_dir / "knowledge.txt"
        if not knowledge_file.exists():
            raise FileNotFoundError(f"Knowledge file not found at {knowledge_file}")
            
        loader = TextLoader(str(knowledge_file))
        documents = loader.load()

        # Create vector embeddings and store them in ChromaDB
        embedding = OpenAIEmbeddings(openai_api_key=api_key)
        vectorstore = Chroma.from_documents(
            documents, 
            embedding,
            persist_directory=str(db_dir)
        )

        # Set up retriever to fetch 3 most relevant chunks per query
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        
        # Create and return the QA chain with OpenAI model
        return RetrievalQA.from_chain_type(
            llm=ChatOpenAI(openai_api_key=api_key),
            chain_type="stuff",  # 'stuff' method passes all retrieved docs to LLM at once
            retriever=retriever
        )
    except Exception as e:
        print(f"Error setting up the QA chain: {str(e)}")
        sys.exit(1)

def main():
    """Main function to run the interactive Q&A system.
    
    Provides a command-line interface for users to ask questions about
    migratory birds, using the knowledge base in data/knowledge.txt.
    Users can exit by typing 'exit' or 'quit', or using Ctrl+C.
    """
    print("\n=== Migratory Birds Knowledge Base Q&A System ===")
    print("Initializing the Q&A system...")
    qa_chain = setup_qa_chain()
    
    print("\nWelcome! You can ask questions about:")
    print("• Basic migration concepts and navigation methods")
    print("• Different types of migration (Latitudinal, Longitudinal, Altitudinal)")
    print("• Notable migratory species and their records")
    print("• Conservation challenges and efforts")
    print("• Migration timing and seasons")
    print("\nExample questions:")
    print("- How do birds navigate during migration?")
    print("- What is the longest known migration route?")
    print("- What challenges do migratory birds face?")
    print("\nType 'exit' or 'quit' to end the session.")
    print("\nAsk your questions about migratory birds!\n")

    while True:
        try:
            # Get user input and handle special commands
            query = input("\nYour question: ").strip()
            if not query:
                continue
                
            if query.lower() in ("exit", "quit"):
                print("\nThank you for using the Migratory Birds Q&A system. Goodbye!")
                break
                
            # Process query and display response
            print("\nSearching knowledge base...")
            response = qa_chain.invoke({"query": query})
            print("\nAnswer:", response["result"])
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    main()
