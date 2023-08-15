####################
from llama_index import download_loader, VectorStoreIndex
#################

from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings

from openai.error import OpenAIError
######################
from base import  ArxivReader_mod
######################

import os
import sys
import openai
import streamlit as st
from  sidebar  import *



# create the website reader
#########ArxivReader= download_loader("ArxivReader")
global loader,documents, index,dummy, test

loader = None
documents = None
index = None


st.set_page_config(page_title="My App")

st.header("ArxivGPT ")
sidebar()



st.header("Please Note!!!")
st.subheader(
     "Due to technical problems  the ArxivGPT is down. We are working to fix the problem."
     "In the meanwhile exactly the same version can be visited in HuggingFace platform."
     "Please click on the link [ArxivGPT](https://huggingface.co/spaces/amanatid/ArxivGPT_Streamlit)."
)




st.subheader(
    "I am an ArxivGPT(Chatbot) Research Scientist. Please fill the fields below to start our discussion....."
    "If you find it useful, you can kindly donate here [Stripe](https://buy.stripe.com/cN2dUu44OahXaJO288)....and "
    "for any problem, please report to the email [amanatid](amanatid@gmail.com)"
)




api_key_input = st.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="Paste your OpenAI API key here.....",
    help="You can get your API key from https://platform.openai.com/account/api-keys.",
)

os.environ['OPENAI_API_KEY'] = api_key_input


query = st.text_input("What scientific topic do you want to discuss?")

max_query = st.number_input("How many papers should i investigate?", step=0)
dummy = st.radio(
    "According to which criterion?",
    ('Relevance', 'LastUpdated', 'SubmittedDate'))




if query and max_query:
    if dummy == 'Relevance':
        search_query_int = 0

    if dummy == "LastUpdated":
        search_query_int = 1

    if dummy == "SubmittedDate":
        search_query_int = 2
    
    
    # load the reader
    loader = ArxivReader_mod()
    documents = loader.load_data(search_query=query, papers_dir="tmp/paper", max_results=max_query,
                                 search_criterion=search_query_int)
    ##############
    openai.api_key = api_key_input
    index = VectorStoreIndex.from_documents(documents)
    ##############
    ####index = GPTVectorStoreIndex.from_documents(documents)
    st.markdown("Arxiv papers are loaded based on the criteria")
    st.session_state["api_key_configured"] = True
   

with st.form("my_form"):
    user = st.text_input("Ask me any question about " + query + ":")
    submitted = st.form_submit_button("Submit")

    try:
        if user and index is not None:
            query_engine = index.as_query_engine()
            response = str(query_engine.query(user))
    except Exception as err:
            st.error("User input or Index Error", err)

       
        
    if submitted:
        try:
            if not st.session_state.get("api_key_configured"):
                st.error("Please configure your OpenAI API key!")
            if not query:
                st.error("Please enter a topic to discuss!")
            if not max_query:
                st.error("Please choose number of files to be loaded!")
            if (st.session_state.get("api_key_configured") and query and max_query):
                st.text_area("Bot 🤖", response, height=500)
        except OpenAIError as e:
            st.error(e._message)
        except (RuntimeError, TypeError, NameError):
            st.error("Runtime/Type/Name Error")
        except OSError as err:
            st.error("OS error:", err)
        except ValueError:
            st.error("Could not convert data to string.")
        except Exception as err:
            st.error(f"Unexpected {err=}, {type(err)=}")
        except ConnectionError as err:
            st.error("Connection Error:", err)
