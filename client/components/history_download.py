import streamlit as st

def render_history_download():
    if st.session_state.get("messages"):
        st.subheader("📜 Download Chat History")

        # Convert chat history to a string
        chat_history = "\n\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages
        )

        # Create a download button
        st.download_button(
            label="Download Chat History",
            data=chat_history,
            file_name="chat_history.txt",
            mime="text/plain"
        )