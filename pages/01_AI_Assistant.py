"""
Page: AI Assistant
Advanced chat interface for guitar-related questions and recommendations
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ai_advisor import AITabAdvisor

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 AI Guitar Assistant")
st.write("Ask me anything about guitar tabs, techniques, and learning strategies!")

# Initialize AI advisor
if "ai_advisor" not in st.session_state:
    st.session_state.ai_advisor = AITabAdvisor()

# Check if OpenAI is configured (optional enhancement)
if st.session_state.ai_advisor.is_configured():
    st.success("✅ AI is powered by OpenAI GPT!")

# Chat interface
st.subheader("💬 Chat")
chat_container = st.container()

# Display conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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
    
    # Get AI response
    with st.spinner("🤔 Thinking..."):
        response = st.session_state.ai_advisor.chat(user_input)
        st.chat_message("assistant").write(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Quick action buttons
st.markdown("---")
st.subheader("⚡ Quick Actions")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🎯 Song Recommendation"):
        with st.spinner("Getting recommendations..."):
            response = st.session_state.ai_advisor.get_tab_recommendation("Intermediate", "rock")
            st.info(response)

with col2:
    if st.button("📚 Learn a Technique"):
        technique = st.selectbox(
            "Choose a technique",
            ["Barre Chord", "Fingerpicking", "Vibrato", "Slide", "Hammer-On"]
        )
        if st.button(f"Explain {technique}", key=f"explain_{technique}"):
            with st.spinner(f"Learning about {technique}..."):
                response = st.session_state.ai_advisor.explain_technique(technique)
                st.info(response)

with col3:
    if st.button("🎸 Chords Library"):
        st.info("Go to **Chords** page to browse 30+ chords with diagrams!")

with col4:
    if st.button("📤 Analyze Song"):
        st.info("Go to **My Songs** page to upload and analyze!")

with col5:
    if st.button("📚 My Collection"):
        st.info("Go to **My Library** to track your progress!")
