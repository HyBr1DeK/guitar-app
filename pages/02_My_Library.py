"""
Page: My Library
Personal collection of saved tabs and learning progress
"""

import streamlit as st

st.set_page_config(page_title="My Library", layout="wide")

st.title("📚 My Tab Library")

# Initialize library in session state
if "library" not in st.session_state:
    st.session_state.library = {
        "favorites": [],
        "learning": [],
        "mastered": []
    }

# Tabs for different collections
tab1, tab2, tab3, tab4 = st.tabs(["⭐ Favorites", "🎓 Currently Learning", "✅ Mastered", "📊 Stats"])

with tab1:
    st.subheader("Your Favorite Tabs")
    if st.session_state.library["favorites"]:
        for idx, tab in enumerate(st.session_state.library["favorites"]):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"🎸 {tab}")
            with col2:
                if st.button("👁️", key=f"view_fav_{idx}"):
                    st.info("Tab viewer would open here")
            with col3:
                if st.button("✕", key=f"remove_fav_{idx}"):
                    st.session_state.library["favorites"].pop(idx)
                    st.rerun()
    else:
        st.info("No favorites yet. Start by searching for songs and adding them here!")

with tab2:
    st.subheader("Songs You're Currently Learning")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        new_song = st.text_input("Add a new song to learn", placeholder="Song - Artist")
    with col2:
        if st.button("➕ Add", use_container_width=True):
            if new_song and new_song not in st.session_state.library["learning"]:
                st.session_state.library["learning"].append(new_song)
                st.success("Added to learning list!")
                st.rerun()
    
    if st.session_state.library["learning"]:
        for idx, song in enumerate(st.session_state.library["learning"]):
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.write(f"🎵 {song}")
            with col2:
                progress = st.slider("Progress", 0, 100, 50, key=f"progress_{idx}")
            with col3:
                if st.button("✓", key=f"master_{idx}"):
                    st.session_state.library["mastered"].append(song)
                    st.session_state.library["learning"].pop(idx)
                    st.success("Moved to Mastered!")
                    st.rerun()
            with col4:
                if st.button("✕", key=f"remove_learn_{idx}"):
                    st.session_state.library["learning"].pop(idx)
                    st.rerun()
    else:
        st.info("No songs in your learning list yet.")

with tab3:
    st.subheader("Songs You've Mastered")
    if st.session_state.library["mastered"]:
        for idx, song in enumerate(st.session_state.library["mastered"]):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"🏆 {song}")
            with col2:
                if st.button("Unmaster", key=f"unmaster_{idx}"):
                    st.session_state.library["mastered"].pop(idx)
                    st.rerun()
    else:
        st.info("Master a song to see it here!")

with tab4:
    st.subheader("📊 Your Learning Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tabs", len(st.session_state.library["favorites"]) + 
                               len(st.session_state.library["learning"]) + 
                               len(st.session_state.library["mastered"]))
    
    with col2:
        st.metric("Mastered", len(st.session_state.library["mastered"]))
    
    with col3:
        st.metric("Learning", len(st.session_state.library["learning"]))
    
    with col4:
        st.metric("Favorites", len(st.session_state.library["favorites"]))
    
    st.markdown("---")
    
    # Progress chart placeholder
    st.info("📈 Visual progress charts would be displayed here")
