from src.helper import repo_ingestion, load_repo, context_aware_splitting, get_embedding
from dotenv import load_dotenv
import os

# we also need langchain's vectordb 
from langchain.vectorstores import Chroma


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


documents = load_repo("repo_dir/")
text_chunks = context_aware_splitting(documents)
embs = get_embedding()


# Finally we store vectors in ChromaDB
vectordb = Chroma.from_documents( documents=text_chunks, # cas -> list_of_docs
                      embedding= embs, # embedding object
                       persist_directory="./db" ) # creates this data directory to store the vectors

# create the local db, inside persist_dir we can find the embs
vectordb.persist() 
