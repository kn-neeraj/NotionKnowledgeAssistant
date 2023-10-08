import os
import openai
from dataloader import notion_data_loader
import test_data
from document_chunks import character_splitter, test_doc_splitter
from document_embeddings import store_embeddings, test_vectordb
import prompt_templates
from retrievalqachain import *
from langchain.chat_models import ChatOpenAI
from dashboard import create_bot_ui
import globalvariables as gv
import shutil
from dashboard import create_bot_ui


global QA_CHAIN

# if os.environ['OPENAI_API_KEY'] == "":
#   print("Error : Please set OPENAI_API_KEY environment variable")

# openai.api_key = os.environ['OPENAI_API_KEY']


def save_openai_api_key():
  if gv.OPENAI_API_KEY:
    ## If User provides OpenAI API key.
    openai.api_key = gv.OPENAI_API_KEY
    print(gv.OPENAI_API_KEY)
  else:
    ## Try from environment variable
    openai.api_key = os.environ['OPENAI_API_KEY']


## Step 1 : Load Notion Database
def load_notion_data():
  documents = notion_data_loader(gv.NOTION_DIRECTORY_DEST_FOLDER)
  print("Number of documents loaded : " + str(len(documents)))
  print("\n")
  return documents


## Step 2 : Create Document Chunks
def create_document_chunks(documents):
  doc_chunks = character_splitter(documents)
  test_doc_splitter(doc_chunks, 1)
  print("\n")
  return doc_chunks


## Step 3 : Create & persist embeddings. Get semantically relevant chunks basis your query.
def create_store_vector_embeddings(doc_chunks):
  vector_db = store_embeddings(doc_chunks)
  print("Vector db with embeddings created.")
  # Testing : Retrieve semantically relevant chunk from vector db using first test prompt.
  # test_vectordb(vector_db, [test_data.test_prompts[0]])
  print("\n")
  return vector_db


## Step 4 : Taking user's query and constructing a prompt using the retrieved documents & passing it to OpenAI LLM for response.

def construct_qa_chain(vector_db):
  llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
  prompt_template = prompt_templates.prompt_template()
  qa_chain = retrievalChainWithPrompt(llm, vector_db, prompt_template)
  ### Testing the tool using our test prompts.
  #test_qa_chain(qa_chain, [test_data.test_prompts[0]])
  return qa_chain


## Utility functions
def setup_qa_chain():
  documents = load_notion_data()
  doc_chunks = create_document_chunks(documents)
  vector_db = create_store_vector_embeddings(doc_chunks)
  qa_chain = construct_qa_chain(vector_db)
  global QA_CHAIN
  QA_CHAIN = qa_chain
  

def response_for_prompt(qa_chain, prompt):
  return retrieve_response(qa_chain, prompt)


## CREATE NOTION BOT UI USING GRADIO.

### Define the rerturn functions.
def api_key_return_fn(input_text) :
  if len(input_text) != 0 and input_text is not None:
    gv.OPENAI_API_KEY = input_text
    print("API key saved.")
    save_openai_api_key()
  else:
    print("No API Key entered. Try again!")

def notiondb_file_return_fn(fileobj) :
  print("Notion zip file uploaded. ")
  # Make directory if does not exist.
  os.makedirs(gv.NOTION_DIRECTORY_DEST_FOLDER, exist_ok=True)

  # unzip & put the unzipped file in destination folder.
  shutil.unpack_archive(fileobj.name,
                        gv.NOTION_DIRECTORY_DEST_FOLDER,
                        format="zip")

  #shutil.copy(fileobj.name, dest_path)
  #zip_file_path = os.path.join(dest_path, fileobj.name)
  print("Notion directory unzip completed.")

  #Setup qa chain.
  setup_qa_chain()

def input_prompt_return_fn(input_prompt) : 
  print(input_prompt)
  global QA_CHAIN
  #Get response basis entered prompt.
  response = response_for_prompt(QA_CHAIN, input_prompt)
  #Resonse object has query, result, & source_documents. Extract result from response object and display in UI.
  return response["result"]

notion_bot_ui = create_bot_ui(api_key_return_fn,notiondb_file_return_fn,  input_prompt_return_fn)
notion_bot_ui.launch(share=True)
## save api key, process notion file upload, process input prompt
