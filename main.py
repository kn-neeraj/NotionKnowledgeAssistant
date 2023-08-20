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


print(os.environ['OPENAI_API_KEY'])
openai.api_key = os.environ['OPENAI_API_KEY']

## Load Notion Database
notion_data = notion_data_loader("Notion_db")
print(len(notion_data))






