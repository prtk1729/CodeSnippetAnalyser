# for repo
from git import Repo
# for context-aware-splitting
from langchain.text_splitter import Language
# loader pertaining to load github repos
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser

# std stuff for chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Embedding step requirement for embs
from langchain.embeddings.openai import OpenAIEmbeddings
# for vectorstore
from langchain.vectorstores import Chroma
# GPT-3.5 Turbo
from langchain.chat_models import ChatOpenAI

# To sustain chat memory, chain is required when impelementing memory
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
import os
from dotenv import load_dotenv

# Clone any github repository
def repo_ingestion(repo_url):
    '''
    Feed the url of the repo to clone it and save inside target folder
    '''
    os.makedirs("repo", exist_ok=True)
    repo_path = "repo/"
    Repo.clone_from(repo_url, to_path=repo_path)


# Load the repo
def load_repo(repo_local_path="./repo_dir", target_path="/ecombot" ):
    # parser is set, to understand the text syntaxes of a given language
    loader = GenericLoader.from_filesystem(
                                            repo_local_path + target_path,
                                            glob = "**/*",
                                            suffixes = [".py"], # multiple language in codebase here I can put other suffixes
                                            parser = LanguageParser(language = Language.PYTHON, 
                                                                    parser_threshold = 500) # min num oif tokens >= 500 to qualify as codebase 
                                            )
    documents = loader.load()
    # print( documents )
    # # since 4 py files, 4 Document-elements in the list
    # len(documents)
    return documents



# Creating Text Splitting
def context_aware_splitting(documents):
    '''
    Args:
        documents: List of Document classes of each python file
    Action:
        Performs context-aware-splitting and tags same text of a given function together
    Returns:
        Returns chunks
    '''
    documents_splitter = RecursiveCharacterTextSplitter.from_language(language = Language.PYTHON,
                                                             chunk_size = 2000,
                                                             chunk_overlap = 200)
    
    text_chunks = documents_splitter.split_documents(documents)
    return text_chunks



# Loading Embedding Model
def get_embedding():
    embedding_obj = OpenAIEmbeddings( disallowed_special=() ) # ignore special chars in codebase
    return embedding_obj