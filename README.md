# ArxivChaBot_StreamLit_Updated GTPVectorIndex
A Chatbot based on openAI and streamlit for Arxiv.



## **Intro**

We create an ArxivChatBot App  using Streamlit, llama_index, Langchain and OpenAI.You need to have an account on OpenAI along
with its available Api key. The ChatBot is trained on a specific query, the number of files and a specific criterion. This ChatBot
is an extension of the  previous related Arxiv repos and is trained based on three parameters:
1. Search query
2. Number of files
3. Search criterion:
    - a)Relevance 
    - b)Last updated 
    - c)Submitt Date 
    
You can find the app on [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://amanatid-arxivchabot-streamlit-streamlit-chatbot-sidebar-2r4zv4.streamlit.app/). In case you find it useful you can donate on [Stripe](https://buy.stripe.com/cN2dUu44OahXaJO288). 

For more info  how the llama indexes and langchain models work, there is a nice two part article by [
Ryan Nguyen-Zero to One: A Guide to Building a First PDF Chatbot with LangChain & LlamaIndex-Part1](https://medium.com/how-ai-built-this/zero-to-one-a-guide-to-building-a-first-pdf-chatbot-with-langchain-llamaindex-part-1-7d0e9c0d62f) and [Part-2 LlamaIndex: How to Use Index Correctly](https://betterprogramming.pub/llamaindex-how-to-use-index-correctly-6f928b8944c6).


### **Quick Start**  
- Input the Open Api-key and press Enter.
- Input Query,number of files and choose Relevance, Last updated or Submitted date and press load.
- The maximum number of files you can enter are 50. 
- When you see the message "Arxiv papers are loaded based on the criteria" you are ready to chat as a User.
- Under the User ask the question and press the Submit button, wait a little and the Chatbot will respond you.

We are using the default chat model from OpenAI ChatGPT-4.

### Issues
In the case of a free OpenAI API key takes time to index the loaded pdf files since a free API key has a restricted [rate limits](https://platform.openai.com/docs/guides/rate-limits/overview). To make the process fast, you can use a paid API key. It is not so fast during the training along with the response from the Chatbot engine. Also, Due to reqular updates from the llama/streamlit team, the app might crash. I try to maintain it up. In any case, please report any problem in the email [amanatid](amanatid@gmail.com).

### Future Prospectives 
We  are looking to improve the layout and be more self-explanatory. Also, we will provide
option to download the requested pdf files along with their abstracts. 

### **References**
1. https://github.com/StanfordVL/arxivbot/
2. https://github.com/emptycrown/llama-hub/blob/main/loader_hub/papers/arxiv/
3. https://llamahub.ai/l/papers-arxiv
4. https://github.com/mmz-001/knowledge_gpt/tree/main
5. https://www.arxiv.org/


