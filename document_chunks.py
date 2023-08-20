### Retrieve only the pieces of document chunks that are relevant to the query because context window of LLMs is limited.

### Different ways to split the documents :
#### Characters, tokens, context aware splitting such Markdown header splitter.

### Parameter needed to be tuned : separated, chunk size, chunk overlap, length function, etc.

from langchain.text_splitter import MarkdownTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter


def markdown_text_splitter(documents):
  markdown_text_splitter = MarkdownTextSplitter(chunk_size=100,
                                                chunk_overlap=0)
  document_chunks = markdown_text_splitter.split_documents(documents)
  return document_chunks


def character_splitter(documents):
  chunk_size = 1024
  chunk_overlap = 5
  text_splitter = CharacterTextSplitter(chunk_size=chunk_size,
                                        chunk_overlap=chunk_overlap,
                                        separator="\n")
  document_chunks = text_splitter.split_documents(documents)
  return document_chunks


def recursive_character_spliter(documents):
  chunk_size = 512
  chunk_overlap = 5
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                 chunk_overlap=chunk_overlap)
  document_chunks = text_splitter.split_documents(documents)
  return document_chunks


def test_doc_splitter(document_chunks, page_index):
  print("******Printing document chunk at index " + str(page_index) +
        " ******")
  print("Number of document chunks : ", len(document_chunks))
  page = document_chunks[page_index]
  print("page content :", page.page_content)
  print("page metadata : ", page.metadata)
  print("***** End resutls *******")
