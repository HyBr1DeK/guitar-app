import streamlit as st
import os
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="Guitar Tab Finder AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3em;
        font-weight: bold;
        color: #FF6B35;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }
    .tab-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #FF6B35;
    }
    .difficulty-easy { color: #2ecc71; font-weight: bold; }
    .difficulty-medium { color: #f39c12; font-weight: bold; }
    .difficulty-hard { color: #e74c3c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "search_history" not in st.session_state:
    st.session_state.search_history = []
if "saved_tabs" not in st.session_state:
    st.session_state.saved_tabs = []

# Sidebar configuration
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1384/1384060.png", width=100)
    st.header("🎸 Controls")
    
    st.markdown("---")
    st.subheader("Search Preferences")
    
    tab_source = st.radio(
        "Preferred Tab Source",
        ["All Sources", "Ultimate Guitar", "Chordify", "Tab Provider"],
        help="Select where to search for tabs"
    )
    
    difficulty = st.multiselect(
        "Filter by Difficulty",
        ["Beginner", "Intermediate", "Advanced"],
        default=["Beginner", "Intermediate", "Advanced"]
    )
    
    tab_type = st.multiselect(
        "Tab Types",
        ["Chords", "Tabs", "Lyrics + Chords", "Video Tabs"],
        default=["Chords", "Tabs"]
    )
    
    st.markdown("---")
    st.subheader("⚙️ Settings")
    show_tuning = st.checkbox("Show standard tuning info", value=True)
    auto_transpose = st.checkbox("Auto-transpose for my key", value=False)
    
    if auto_transpose:
        capo_key = st.selectbox(
            "Preferred Starting Key",
            ["C", "D", "E", "F", "G", "A", "B"]
        )

# Main content
st.markdown('<div class="main-header">🎵 Guitar Tab Finder AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask me for any song\'s guitar tabs - I\'ll find them for you!</div>', unsafe_allow_html=True)

# Main search interface
col1, col2 = st.columns([3, 1])

with col1:
    user_query = st.text_input(
        "🔍 Search for a song",
        placeholder="e.g., 'Wonderwall by Oasis' or 'Stairway to Heaven'",
        label_visibility="collapsed"
    )

with col2:
    search_button = st.button("🔎 Find Tabs", use_container_width=True, type="primary")

# Search logic
if search_button and user_query:
    with st.spinner(f"🤖 Searching for tabs for '{user_query}'..."):
        st.session_state.search_history.append({
            "query": user_query,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Placeholder for AI integration
        st.success(f"✅ Found results for: {user_query}")
        
        # Display sample results (placeholder)
        st.subheader(f"Results for '{user_query}'")
        
        tabs = st.tabs(["📊 Results", "📝 Details", "💾 Save"])
        
        with tabs[0]:
            # Sample result cards
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div class="tab-card">
                    <h3>Wonderwall - Oasis</h3>
                    <p><strong>Type:</strong> Chords</p>
                    <p><strong>Difficulty:</strong> <span class="difficulty-easy">Beginner</span></p>
                    <p><strong>Rating:</strong> ⭐⭐⭐⭐⭐ (4.8/5)</p>
                    <p><strong>Source:</strong> Ultimate Guitar</p>
                    <p><strong>Key:</strong> Em7 | Capo: 2nd fret</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("View Full Tab", key="tab1"):
                    st.info("Tab preview would load here with chords and lyrics")
            
            with col2:
                st.markdown(f"""
                <div class="tab-card">
                    <h3>Wonderwall - Oasis</h3>
                    <p><strong>Type:</strong> Full Tabs</p>
                    <p><strong>Difficulty:</strong> <span class="difficulty-medium">Intermediate</span></p>
                    <p><strong>Rating:</strong> ⭐⭐⭐⭐ (4.5/5)</p>
                    <p><strong>Source:</strong> Tab Provider</p>
                    <p><strong>Key:</strong> Em7 | Capo: 2nd fret</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("View Full Tab", key="tab2"):
                    st.info("Tab preview would load here with detailed fingering")
        
        with tabs[1]:
            st.write("**Song Information:**")
            st.write("- Artist: Oasis")
            st.write("- Album: (What's the Story) Morning Glory?")
            st.write("- Year: 1994")
            st.write("- BPM: 86")
            st.write("- Original Key: Em7")
        
        with tabs[2]:
            if st.button("💾 Save to My Collection"):
                st.session_state.saved_tabs.append(user_query)
                st.success("✅ Tab saved!")

# Display search history
if st.session_state.search_history:
    st.markdown("---")
    with st.expander("📜 Recent Searches"):
        for item in reversed(st.session_state.search_history[-10:]):
            st.write(f"🕐 {item['timestamp']} - {item['query']}")

# Display saved tabs
if st.session_state.saved_tabs:
    st.markdown("---")
    with st.expander("💾 My Saved Tabs"):
        for tab in st.session_state.saved_tabs:
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"🎸 {tab}")
            with col2:
                if st.button("✕", key=f"remove_{tab}"):
                    st.session_state.saved_tabs.remove(tab)
                    st.rerun()

# Info section
st.markdown("---")
st.info("""
**💡 How to use:**
1. Enter a song name and artist (e.g., "Hotel California by Eagles")
2. Browse through available tabs from different sources
3. View difficulty levels, ratings, and user reviews
4. Save your favorite tabs for quick access
5. Transpose tabs to your preferred key

**🚀 Features Coming Soon:**
- AI-powered tab recommendations based on your skill level
- Video tutorials integrated with tabs
- Chord difficulty analyzer
- Practice mode with BPM control
""")

st.markdown("---")
st.caption("🎸 Guitar Tab Finder AI | Powered by OpenAI & Tab Databases | Made with ❤️")
