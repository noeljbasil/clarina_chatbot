import streamlit as st
from streamlit_chat import message
from src.langchain_agent import init, init_agent

def main():
    
    #initialise agent and streamlit page
    init()
    agent_executor = init_agent()
    
    # initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # store agent in memory
    if "clarina" not in st.session_state:
        st.session_state.clarina = agent_executor

    # store generated responses in memory
    if 'generated' not in st.session_state:
        st.session_state.generated = []
    
    # define function to generate response
    def generate_response(user_input):
        # handle user input
        if user_input:
            # save user input
            st.session_state.messages.append(user_input) 
            # get response from agent
            with st.spinner("Thinking..."):
                response = st.session_state.clarina.run(user_input)
            # save response
            st.session_state.messages.append(response) 
            st.session_state.generated.append(response)    

    # container for chat history
    response_container = st.container()
    # container for text box
    container = st.container()

    with container:

        # initialize session state to clear input text box after user enters input
        if "temp" not in st.session_state:
            st.session_state.temp = ""

        def clear_text():
            """callback function to clear input text box"""
            st.session_state.temp = st.session_state.user_input
            st.session_state.user_input = ""

        st.text_input("user input",key="user_input",placeholder = "Enter your question here", label_visibility="hidden",on_change=clear_text) # get user input
        generate_response(st.session_state.temp) # generate response

    # display message history
    if st.session_state.generated:
        
        with response_container:
            messages = st.session_state.get('messages', []) 
            for i, msg in enumerate(messages):
                if i % 2 == 0:
                    # display user input
                    message(msg, is_user=True, key=str(i) + '_user')
                else:
                    # display response
                    message(msg, is_user=False, key=str(i) + '_ai')    

if __name__ == '__main__':
    main()