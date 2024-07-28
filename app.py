
from git import Repo
from langchain.text_splitter import Language
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from flask import Flask, render_template, jsonify, request

import os
from dotenv import load_dotenv
from src.helper import get_embedding, repo_ingestion

app = Flask(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


embs = get_embedding()
persist_directory = "db"
vectordb = Chroma(persist_directory=persist_directory, \
       embedding_function=embs)


llm = ChatOpenAI() # default i.e 3.5 turbo
memory = ConversationSummaryMemory( llm = llm, \
                                   memory_key="chat_history",
                                   return_messages=True)
qa = ConversationalRetrievalChain.from_llm( llm = llm,\
                                           retriever=vectordb.as_retriever(search_type="mmr",
                                                                           search_kwargs={"k": 3}),
                                            memory=memory )


# define the routes
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/chatbot", methods=["GET", "POST"])
def gitRepo():
    '''
    - Entire pipeline is invoked
    - Repo url is ingested
    - Clones repo -> CAS -> Embeddings -> The repo is stored as vectors
    based on the embedding_obj persistently
    '''
    if request.method == "POST":
        repo_url_from_user = request.form['question']
        repo_ingestion(repo_url_from_user)
        # based on the url ingested repo
        # call the pipeline to create the vectordb
        os.system("python3 store_index.py")
    return jsonify({"response": str(repo_url_from_user)})


@app.route('/get', methods=["GET", "POST"])
def chat():
    input_msg = request.form["msg"]
    print(input_msg)

    # clearing previously persisting repo-db
    if input_msg == "clear":
        os.system("rm -rf repo_dir")

    result = qa(input_msg)
    answer = result["answer"]
    print( answer )
    return str(answer)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=8080, debug=True)