### Create a langchain retrieval chain which will get similar documentts from specified vector db using the query.
### Then passes the prompt constructed from the query to the specified LLM and retrieves the response.

from langchain.chains import RetrievalQA

def retrievalChain(llm, vectordb):
  qa_chain = RetrievalQA.from_chain_type(llm,
                                         chain_type="stuff",
                                         retriever=vectordb.as_retriever(),
                                         return_source_documents=True)
  return qa_chain


def retrievalChainWithPrompt(llm, vectordb, prompt_template):
  qa_chain = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt_template})
  return qa_chain

def test_qa_chain(qa_chain, prompt):
  print("Prompt : " + prompt)
  result = qa_chain({"query": prompt})
  print(result["result"])
  # print("*** Printing Source Documents ***")
  # for source_document in result["source_documents"]:
  #   print(source_document)