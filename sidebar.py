import streamlit as st

from faq import faq


#def set_openai_api_key(api_key: str):
#    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Choose the Scientific Topic to dicuss🚩\n"
            "3. Load the number of  papers you want to investigate. \n"
            "4. Choose a criterion.\n"
            "5. Wait for the message 'Arxiv papers are loaded based on the criteria' to be appeared.\n"
        )

        '''
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)
        '''
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📚ArxivGPT allows you to  commit a scientific dialogue based on"
            " a specific  question/criterion and the amount of data that are loaded from"
            "[arxiv.org](https://arxiv.org/). "
        )
        st.markdown(
            "This is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/amanatid/ArxivChatBot_StreamlitApp) " 
            "with your feedback and suggestions💡. Due to regular upgrades from llama or streamilit team, the app maybe 
            sometimes crashes. I try to keep it on a continous updated basis but in any case please, contact me on the email
            below."
        )
        st.markdown("Made by [amanatid](amanatid@gmail.com)")
        st.markdown("---")

        faq()
