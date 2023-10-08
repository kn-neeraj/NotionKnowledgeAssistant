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


def retrieve_response(qa_chain, prompt):
  return qa_chain({"query": prompt})


def test_qa_chain(qa_chain, prompts):
  print("*** Testing QA bot using test prompts.***")
  for test_prompt in prompts:
    print("Test Prompt : " + test_prompt)
    print("\n")
    print("Bot Response : " + qa_chain({"query": test_prompt})["result"])
    print("\n")
  print("*** Finished testing QA bot with test prompts***")
