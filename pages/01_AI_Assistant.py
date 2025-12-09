"""
Page: AI Assistant
Advanced chat interface for guitar-related questions and recommendations
"""

import streamlit as st

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 AI Guitar Assistant")
st.write("Ask me anything about guitar tabs, techniques, and learning strategies!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat interface
st.subheader("💬 Chat")
chat_container = st.container()

# Display conversation history
for message in st.session_state.chat_history:
    with chat_container:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

# Input for new message
user_input = st.chat_input("Ask me about guitar tabs, techniques, or learning...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Get AI response (placeholder)
    response = "I'd be happy to help! In production, this would be powered by OpenAI's GPT model. " \
               "For now, feel free to ask about: song recommendations, guitar techniques, practice tips, or learning strategies!"
    
    st.chat_message("assistant").write(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Quick action buttons
st.markdown("---")
st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎯 Get Song Recommendation"):
        st.info("Tell me your skill level and music preference!")

with col2:
    if st.button("📚 Learn a Technique"):
        technique = st.selectbox(
            "Choose a technique",
            ["Barre Chord", "Fingerpicking", "Vibrato", "Slide", "Hammer-On"]
        )

with col3:
    if st.button("📋 Generate Practice Plan"):
        st.info("Select a song and your current skill level to get a personalized plan!")
