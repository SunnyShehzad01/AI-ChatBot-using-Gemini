import streamlit as st
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv('google_api_key'))
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h2 style='text-align: center;'>Gemini 🤖 ChatBot</h2>", unsafe_allow_html=True)


# Lets initiate the memory
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- Clear Chat Button ---
if st.button("🧹 Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()

# Display the chat
for chat in st.session_state.chat_history:
    with st.chat_message(chat['role']):
        st.markdown(chat['content'])

user_input = st.chat_input("Enter your message")

if user_input:
    st.chat_message('user').markdown(user_input)
    st.session_state.chat_history.append({'role':'user', 'content':user_input})

    gemini_history = [{'role': msg['role'], 'parts':msg['content']} for msg in st.session_state.chat_history]
    response = model.generate_content(gemini_history)
    bot_reply = response.text
    st.chat_message('assistant').markdown(bot_reply)
    st.session_state.chat_history.append({'role':'assistant', 'content':bot_reply})