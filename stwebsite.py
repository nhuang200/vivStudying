import streamlit as st

def main():
    st.set_page_config(
        page_title="HI",
        page_icon="🎥",
        layout="wide"
    )

    # Initialize session state (simplified)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Title
    st.title("Hi Viv! Good Job Studying SO hard! I LOVE YOU!!")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTZjMDliOTUyYTgzbnU0ZjgxcGpqaGZhZWVjMGYyZGl6eHdmNDVvdDU3ZHh4ajdodyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KztT2c4u8mYYUiMKdJ/giphy.gif", width=400, caption="You're doing great!")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message:
                with st.expander("Sources (with similarity scores)"):
                    for source, score in zip(message["sources"], message["scores"]):
                        st.markdown(f"- {source} (Score: {score:.4f})")

    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("nathan"):
            with st.spinner("Thinking..."):
                try:
                    # Display answer
                    st.markdown("I LOVE YOU") 
                    # Just a fixed message

                    # Save to history (including sources if needed)
                    st.session_state.messages.append({
                        "role": "nathan",
                        "content": "I Love You",
                    })

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Sidebar: Show top documents with scores for last question
    with st.sidebar:
        st.subheader("I Love You")

if __name__ == "__main__":
    main()

