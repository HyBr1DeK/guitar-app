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
# Placeholder for technique explanations (separate from the chat UI)
technique_placeholder = st.empty()

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
    if st.button("🎯 Song Recommendation", use_container_width=True):
        with st.spinner("Getting recommendations..."):
            response = st.session_state.ai_advisor.get_tab_recommendation("Intermediate", "rock")
            st.info(response)

with col2:
    if st.button("📚 Learn a Technique", use_container_width=True):
        st.session_state.show_technique_selector = True

if st.session_state.get("show_technique_selector", False):
    st.divider()
    st.subheader("🎵 Choose a Technique to Learn")
    
    technique = st.selectbox(
        "Select a technique:",
        ["Barre Chord", "Fingerpicking", "Vibrato", "Slide", "Hammer-On", "Pull-Off", "Bend", "Palm Mute"],
        key="technique_select"
    )
    
    if st.button("📖 Learn & Get Answer", use_container_width=True):
        with st.spinner(f"Loading {technique} details..."):
            # Remove any prior assistant messages that contain technique overviews
            technique_names = ["vibrato", "hammer-on", "hammer on", "pull-off", "pull off", "slide", "bend", "palm mute", "fingerpicking", "barre"]
            new_history = []
            for msg in st.session_state.chat_history:
                if msg.get("role") == "assistant":
                    content_lower = msg.get("content", "").lower()
                    raw_content = msg.get("content", "")
                    # Only remove assistant messages that are likely technique-overviews (contain the guitar emoji and technique keywords)
                    if ("🎸" in raw_content and (any(name in content_lower for name in technique_names) or "advanced guitar techniques" in content_lower)):
                        # skip (remove) assistant messages that are technique-overviews
                        continue
                new_history.append(msg)
            st.session_state.chat_history = new_history

            # Display the requested technique explanation in its own placeholder
            response = st.session_state.ai_advisor.explain_technique(technique)
            technique_placeholder.empty()
            with technique_placeholder:
                with st.expander(f"📚 Mastering {technique}", expanded=True):
                    st.markdown(response)
    
    st.divider()
    if st.button("❌ Close & Hide", use_container_width=True):
        st.session_state.show_technique_selector = False
        technique_placeholder.empty()
        st.rerun()

with col3:
    if st.button("🎸 Chords Library", use_container_width=True):
        st.switch_page("pages/06_Chords.py")

with col4:
    if st.button("📤 Analyze Song", use_container_width=True):
        st.switch_page("pages/05_My_Songs.py")

with col5:
    if st.button("📚 My Collection", use_container_width=True):
        st.switch_page("pages/02_My_Library.py")
