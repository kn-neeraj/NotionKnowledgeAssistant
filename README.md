## Asking LLMs to answer questions based on your private data soureces using Request Augmented Generation (RAG) technique.

### Why Request Augmented Generation (RAG)? 
Suppose you have your data repository (example - Notion Notes) and you want to be able QnA using prompts. Base (pre-trained) Large Language Models are only aware of the information they are pre-trained on. Base LLM's answers to prompts based on your private data will fall short or even hallucinate.

### What is Request Augmented Generation (RAG)? 
Request Augmented Generation (RAG) fetches relevant information basis your prompt from your data source and enhances the input prompt to LLM, providing richer context to improve LLM ouput. It combines the power of existing Information Retrieval techniques and LLMs by fetching relevant documents from your provided data repository and augment the final prompt to base LLM to improve factuality in LLM answers and reduce hallucination.

### How it works?
![LLM RAG Technique](./resources/LLM-RAG.png)
