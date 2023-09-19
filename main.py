import os
import openai
from dataloader import notion_data_loader
import test_data
from document_chunks import character_splitter, test_doc_splitter
from document_embeddings import store_embeddings, test_vectordb
import prompt_templates
from retrievalqachain import retrievalChainWithPrompt, test_qa_chain
from langchain.chat_models import ChatOpenAI

if os.environ['OPENAI_API_KEY'] == "":
  print("Error : Please set OPENAI_API_KEY environment variable")

openai.api_key = os.environ['OPENAI_API_KEY']

## Step 1 : Load Notion Database
documents = notion_data_loader("Notion_db")
print("Number of documents loaded : " + str(len(documents)))
print("\n")

## Step 2 : Create Document Chunks
doc_chunks = character_splitter(documents)
test_doc_splitter(doc_chunks, 1)
print("\n")

## Step 3 : Create & persist embeddings. Get semantically relevant chunks basis your query.
vector_db = store_embeddings(doc_chunks)
# Testing : Retrieve semantically relevant chunk from vector db using first test prompt.
test_vectordb(vector_db, [test_data.test_prompts[0]])

## Step 4 : Taking user's query and constructing a prompt using the retrieved documents & passing it to OpenAI LLM for response.

# llm  = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
# prompt_template = prompt_templates.prompt_template()
# qa_chain = retrievalChainWithPrompt(llm, vector_db, prompt_template)

## QnA
# test_qa_chain(qa_chain, test_data.test_prompts[2])
