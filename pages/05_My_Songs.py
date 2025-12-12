"""
Page: My Songs
Upload and analyze songs with chord progression analysis
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ai_advisor import AITabAdvisor

st.set_page_config(page_title="My Songs", layout="wide")

st.title("🎵 My Songs")
st.write("Upload your song files to analyze chords and get personalized learning tips!")

# Initialize AI advisor
if "ai_advisor" not in st.session_state:
    st.session_state.ai_advisor = AITabAdvisor()

# Initialize my songs in session state
if "my_songs" not in st.session_state:
    st.session_state.my_songs = []

# File upload section
st.subheader("📤 Upload Your Song")

col1, col2 = st.columns([3, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Choose a song file (TXT, MD, or paste text)",
        type=["txt", "md"],
        help="Upload a file with song lyrics and chords"
    )

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    use_text_input = st.checkbox("Paste text instead")

# Handle file upload or text input
song_content = None
song_name = None

if use_text_input:
    st.subheader("Paste Your Song Here")
    song_name = st.text_input("Song name", placeholder="e.g., Wonderwall")
    song_content = st.text_area(
        "Paste song lyrics with chords",
        placeholder="""[Am]
I'd like to be under the sea
[F]
In the octopus's garden in the shade
[C]
He let us in...""",
        height=250
    )
    
    if st.button("Analyze Song", type="primary", use_container_width=True):
        if song_content and song_name:
            with st.spinner("🤖 Analyzing chords..."):
                analysis = st.session_state.ai_advisor.analyze_song_chords(song_content, song_name)
                st.markdown(analysis)
                
                # Save to my songs
                if song_name not in [s["name"] for s in st.session_state.my_songs]:
                    st.session_state.my_songs.append({
                        "name": song_name,
                        "content": song_content,
                        "analysis": analysis
                    })
                    st.success(f"✅ '{song_name}' saved to your collection!")
        else:
            st.warning("Please enter both a song name and content!")

elif uploaded_file:
    song_name = uploaded_file.name.replace(".txt", "").replace(".md", "")
    song_content = uploaded_file.read().decode("utf-8")
    
    st.subheader(f"📋 Analyzing: {song_name}")
    
    # Show file preview
    with st.expander("📄 File Preview"):
        st.text(song_content[:500] + "..." if len(song_content) > 500 else song_content)
    
    # Analyze button
    if st.button("🔍 Analyze Chords", type="primary", use_container_width=True):
        with st.spinner("🤖 Analyzing chords..."):
            analysis = st.session_state.ai_advisor.analyze_song_chords(song_content, song_name)
            st.markdown(analysis)
            
            # Save to my songs
            if song_name not in [s["name"] for s in st.session_state.my_songs]:
                st.session_state.my_songs.append({
                    "name": song_name,
                    "content": song_content,
                    "analysis": analysis
                })
                st.success(f"✅ '{song_name}' saved to your collection!")

# My Songs Collection
st.markdown("---")
st.subheader("📚 Your Song Collection")

if st.session_state.my_songs:
    # Tabs for each song
    song_names = [song["name"] for song in st.session_state.my_songs]
    tabs = st.tabs([f"🎵 {name}" for name in song_names])
    
    for idx, tab in enumerate(tabs):
        with tab:
            song = st.session_state.my_songs[idx]
            
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**Song:** {song['name']}")
            
            with col2:
                if st.button("📝 Edit", key=f"edit_{idx}"):
                    st.session_state.editing = idx
            
            with col3:
                if st.button("🗑️ Delete", key=f"delete_{idx}"):
                    st.session_state.my_songs.pop(idx)
                    st.rerun()
            
            # Show analysis
            st.markdown(song["analysis"])
            
            # Show content
            with st.expander("📄 Show Full Content"):
                st.text(song["content"])

else:
    st.info("""
    📤 **No songs uploaded yet!**
    
    Upload or paste a song with chords to:
    - Get automatic chord analysis
    - See difficulty level
    - Get personalized learning tips
    - Track your practice songs
    """)

# Quick tips
st.markdown("---")
st.subheader("💡 Upload Tips")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Supported Formats:**
    - Plain text (.txt)
    - Markdown (.md)
    - Pasted text
    
    **File Size:** Up to 200MB
    """)

with col2:
    st.write("""
    **Best Format for Analysis:**
    ```
    [Am] Chord name
    Lyrics here
    [F] Next chord
    More lyrics
    ```
    """)
