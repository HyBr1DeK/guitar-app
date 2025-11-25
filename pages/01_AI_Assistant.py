"""
Page: AI Assistant
Advanced chat interface for guitar-related questions and recommendations
"""

import streamlit as st
from utils.ai_advisor import AITabAdvisor

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 AI Guitar Assistant")
st.write("Ask me anything about guitar tabs, techniques, and learning strategies!")

# Initialize AI advisor
if "ai_advisor" not in st.session_state:
    st.session_state.ai_advisor = AITabAdvisor()

# Chat interface
st.subheader("💬 Chat")
chat_container = st.container()

# Display conversation history
for message in st.session_state.ai_advisor.conversation_history:
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
    
    # Get AI response
    with st.spinner("Thinking..."):
        response = st.session_state.ai_advisor.chat(user_input)
        st.chat_message("assistant").write(response)

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
