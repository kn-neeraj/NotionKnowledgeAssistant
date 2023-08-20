from langchain.prompts import PromptTemplate

#Build a prompt for retrieval QA.
retrievalQA_template =   """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Provide answers in bullet points. Max 10 bullet points. Always say "Thanks for asking!" at the end of the answer. 
  {context}
  Question: {question}
  Helpful Answer:"""

def prompt_template() : 
  return PromptTemplate.from_template(retrievalQA_template)