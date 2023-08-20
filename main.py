#Objective : Create a personal knowledge chatbot based on my knowledge base from Notion.
# 0. Load the data
# 1. Separating the big document into semantically relevant document chunks
# 2. Create embeddings from document chunks
# 3. Store in a vector store and persist it
# 4. Retrieve relevant chunks from the vector store basis the query
# 5. Pass the query + relevant document chunk to LLM
# 6. Support history to ensure subsequent prompts have context from previous
# 7. Support UI way of doing this!

import os
import openai
from dataloader import notion_data_loader
import test_data
from document_chunks import character_splitter, test_doc_splitter
from document_embeddings import store_embeddings, test_vectordb
import prompt_templates
from retrievalqachain import retrievalChainWithPrompt, test_qa_chain
from langchain.chat_models import ChatOpenAI

print(os.environ['OPENAI_API_KEY'])
openai.api_key = os.environ['OPENAI_API_KEY']

## Load Notion Database
documents = notion_data_loader("Notion_db")
# print(len(documents))

## Create Document Chunks
doc_chunks = character_splitter(documents)
# test_doc_splitter(doc_chunks, 1)

## Create & persist embeddings. Get semantically relevant chunks basis query.
vector_db = store_embeddings(doc_chunks)
# test_vectordb(vector_db, test_data.test_prompts)

## Retrieval QA chain 
llm  = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
prompt_template = prompt_templates.prompt_template()
qa_chain = retrievalChainWithPrompt(llm, vector_db, prompt_template)

## QnA
test_qa_chain(qa_chain, test_data.test_prompts[2])

