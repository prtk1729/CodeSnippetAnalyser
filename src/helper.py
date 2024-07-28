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


