"""
Page: Chords Library
Browse 30+ guitar chords with visual diagrams and finger positions
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(page_title="🎸 Chords Library", layout="wide")

st.title("🎸 Guitar Chords Library")
st.write("Explore 30+ guitar chords with visual diagrams, finger positions, and tips!")

# Chord database with detailed information
CHORDS_DB = {
    # Major Chords
    "C Major": {
        "category": "Major Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret A string) | 2nd finger (2nd fret D string) | 3rd finger (3rd fret B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ 1 2 │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X 3 2 0 1 0
        """,
        "tips": "Start with this chord! One of the easiest open chords.",
        "used_in": "Wonderwall, Knockin' On Heaven's Door, Blackbird"
    },
    
    "G Major": {
        "category": "Major Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (2nd fret A string) | 2nd finger (3rd fret high E string) | 3rd finger (3rd fret low B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 3 │ │ │ 2 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ 1 │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 3 2 0 0 0 3
        """,
        "tips": "Great for rock and pop songs. Practice smooth transitions.",
        "used_in": "Three Little Birds, Horse With No Name, Brown Eyed Girl"
    },
    
    "D Major": {
        "category": "Major Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret D string) | 2nd finger (2nd fret high E string) | 3rd finger (2nd fret B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ 1 2 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X X 0 2 3 2
        """,
        "tips": "Essential beginner chord. Great for folk and acoustic.",
        "used_in": "Wonderwall, To Build a Home, House of the Rising Sun"
    },
    
    "A Major": {
        "category": "Major Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret D string) | 2nd finger (2nd fret G string) | 3rd finger (2nd fret B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 1 │ │ 2 3 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 0 2 2 2 0
        """,
        "tips": "Very common chord. Practice smooth transitions with E.",
        "used_in": "Smells Like Teen Spirit, Sweet Home Alabama, Zombie"
    },
    
    "E Major": {
        "category": "Major Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret G string) | 2nd finger (2nd fret D string) | 3rd finger (2nd fret B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ 2 1 3 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 2 2 1 0 0
        """,
        "tips": "Powerful open chord. Great for rock and blues.",
        "used_in": "House of the Rising Sun, Sweet Home Chicago, Layla"
    },
    
    # Minor Chords
    "A Minor": {
        "category": "Minor Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret B string) | 2nd finger (2nd fret G string) | 3rd finger (2nd fret D string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ 2 1 3 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 0 2 2 1 0
        """,
        "tips": "Easiest minor chord! Great starting point.",
        "used_in": "Wonderwall, House of the Rising Sun, Zombie"
    },
    
    "E Minor": {
        "category": "Minor Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (2nd fret A string) | 2nd finger (2nd fret D string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ 1 2 │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 2 2 0 0 0
        """,
        "tips": "Only 2 fingers! Very easy and sounds beautiful.",
        "used_in": "Wonderwall, Hallelujah, Fade to Black"
    },
    
    "D Minor": {
        "category": "Minor Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (1st fret high E string) | 2nd finger (2nd fret G string) | 3rd finger (3rd fret B string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 1 │ │ 2 │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X X 0 2 3 1
        """,
        "tips": "Great warm sound. Common in folk and rock.",
        "used_in": "House of the Rising Sun, Mad World, Creep"
    },
    
    # Seventh Chords
    "G7": {
        "category": "Seventh Chords",
        "difficulty": "Intermediate",
        "finger_positions": "1st finger (2nd fret A string) | 2nd finger (3rd fret high E string) | 3rd finger (3rd fret B string) | 4th finger (3rd fret D string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 3 │ 4 │ 2 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ 1 │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 3 2 0 0 0 1
        """,
        "tips": "Bluesy sound. Perfect for blues and rock.",
        "used_in": "Johnny B Goode, Sweet Home Chicago, Ramblin' Man"
    },
    
    "D7": {
        "category": "Seventh Chords",
        "difficulty": "Intermediate",
        "finger_positions": "1st finger (1st fret high E string) | 2nd finger (2nd fret high B string) | 3rd finger (2nd fret D string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 1 │ │ 2 3 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X X 0 2 1 2
        """,
        "tips": "Often used before G in blues progressions.",
        "used_in": "All blues songs, Dust in the Wind, Bad Moon Rising"
    },
    
    "A7": {
        "category": "Seventh Chords",
        "difficulty": "Intermediate",
        "finger_positions": "1st finger (1st fret D string) | 2nd finger (2nd fret G string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ 1 2 │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 0 2 0 2 0
        """,
        "tips": "Great blues chord. Common progression: A7 - D7 - E7",
        "used_in": "Mannish Boy, Stormy Monday, All Blues Tunes"
    },
    
    # Barre Chords (Intermediate)
    "F Major": {
        "category": "Barre Chords",
        "difficulty": "Advanced",
        "finger_positions": "1st finger (1st fret - all strings, barre) | 2nd finger (2nd fret A string) | 3rd finger (3rd fret D string) | 4th finger (3rd fret high E string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ 1 1 1 1 1 1 │ (Barre!)
        │ ├─┼─┼─┼─┼─┤
        │ │ 2 │ │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ 4 │ │ │
        │ └─────────────┘
        
        Barre 1st - 1 3 3 2 1 1
        """,
        "tips": "THE challenging barre chord! Practice 15 min daily. Worth it!",
        "used_in": "Wonderwall (capo 2), Pink Floyd songs, Many classics"
    },
    
    "B Minor": {
        "category": "Barre Chords",
        "difficulty": "Advanced",
        "finger_positions": "1st finger (2nd fret - barre) | 2nd finger (3rd fret A string) | 3rd finger (4th fret D string) | 4th finger (4th fret high E string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ 1 1 1 1 1 │ (Barre!)
        │ ├─┼─┼─┼─┼─┤
        │ │ 2 │ │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ 4 │ │ │
        │ └─────────────┘
        
        Barre 2nd - 2 4 4 3 2 2
        """,
        "tips": "Easier than F. Progress after mastering F chord.",
        "used_in": "Come Together, Angie, Black Hole Sun"
    },
    
    # Power Chords
    "E5 (Power Chord)": {
        "category": "Power Chords",
        "difficulty": "Beginner",
        "finger_positions": "1st finger (root note) | 2nd finger (5th fret up on adjacent string)",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ 1 │ │ 2 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Low E string - 0 2 2
        """,
        "tips": "Easy and powerful! Perfect for rock and metal.",
        "used_in": "Smoke on the Water, Enter Sandman, Iron Man"
    },
    
    # Additional Chords
    "Cmaj7": {
        "category": "Jazz/Extended",
        "difficulty": "Intermediate",
        "finger_positions": "Simple open position with added finger",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ 1 2 │ 3 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X 3 2 0 0 0
        """,
        "tips": "Beautiful jazz chord. Adds sophistication.",
        "used_in": "Make It With You, Girl from Ipanema, Standard Jazz"
    },
    
    "Am7": {
        "category": "Extended Chords",
        "difficulty": "Beginner",
        "finger_positions": "Similar to Am, open position",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ 1 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ 2 │ │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - 0 0 2 0 1 0
        """,
        "tips": "Softer than Am. Used in Wonderwall!",
        "used_in": "Wonderwall, Smooth Criminal, Black Hole Sun"
    },
    
    "Dm7": {
        "category": "Extended Chords",
        "difficulty": "Beginner",
        "finger_positions": "Open position variation",
        "diagram": """
        E A D G B e
        ┌─────────────┐
        │ │ │ │ │ 1 │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ 2 3 │ │
        │ ├─┼─┼─┼─┼─┤
        │ │ │ │ │ │ │
        │ └─────────────┘
        
        Open - X X 0 2 1 1
        """,
        "tips": "Great chord for modern songs.",
        "used_in": "Creep, Zombie, Paranoid Android"
    },
}

# Organize chords by category
categories = {}
for chord_name, chord_data in CHORDS_DB.items():
    category = chord_data["category"]
    if category not in categories:
        categories[category] = []
    categories[category].append(chord_name)

# Sidebar - Quick search
with st.sidebar:
    st.subheader("🔍 Quick Chord Search")
    
    # Dropdown to select a chord
    chord_names = list(CHORDS_DB.keys())
    selected_chord_dropdown = st.selectbox(
        "Choose a chord to learn:",
        chord_names,
        index=0,
        key="chord_dropdown"
    )
    
    if selected_chord_dropdown:
        st.session_state.selected_chord = selected_chord_dropdown
    
    st.markdown("---")
    st.subheader("📂 Filter by Category")
    selected_category = st.radio(
        "Select category",
        ["All Chords"] + list(categories.keys()),
        index=0
    )

# Main content
st.subheader("📚 Browse All Chords")

# Filter chords based on category selection
if selected_category == "All Chords":
    filtered_chords = list(CHORDS_DB.keys())
else:
    filtered_chords = categories[selected_category]

# Display chords in a grid
col1, col2, col3 = st.columns(3)
for idx, chord_name in enumerate(filtered_chords):
    col = [col1, col2, col3][idx % 3]
    
    with col:
        if st.button(f"🎸 {chord_name}", use_container_width=True, key=f"btn_{chord_name}"):
            st.session_state.selected_chord = chord_name

# Show selected chord details
if "selected_chord" in st.session_state:
    chord_name = st.session_state.selected_chord
    chord_data = CHORDS_DB[chord_name]
    
    st.markdown("---")
    st.subheader(f"🎸 {chord_name} - Detailed View")
    
    # Chord info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Category", chord_data["category"])
    
    with col2:
        difficulty_emoji = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}
        emoji = difficulty_emoji.get(chord_data["difficulty"], "❓")
        st.metric("Difficulty", f"{emoji} {chord_data['difficulty']}")
    
    with col3:
        st.metric("Strings", "6")
    
    with col4:
        st.metric("Type", "Guitar")
    
    # Chord diagram
    st.subheader("📐 Chord Diagram & Finger Positions")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Visual Diagram:**")
        st.code(chord_data["diagram"], language="text")
    
    with col2:
        st.write("**How to Play:**")
        st.write(chord_data["finger_positions"])
        
        st.write("\n**🎯 Pro Tips:**")
        st.success(chord_data["tips"])
    
    # Practice info
    st.subheader("🎵 Songs Using This Chord")
    st.write(chord_data["used_in"])
    
    # Practice tips
    st.subheader("📝 Practice Tips")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        ✓ **Daily Practice:**
        - 10-15 minutes per day
        - Focus on clean sound
        - Work on smooth transitions
        """)
    
    with col2:
        st.write("""
        ✓ **Progressive Learning:**
        - Master one chord at a time
        - Practice transitions early
        - Combine with other chords
        """)
    
    # Visual aide
    st.subheader("🎯 Learning Path")
    
    if chord_data["difficulty"] == "Beginner":
        st.success("✅ **Great Starting Point!** Focus on clear sound and smooth transitions.")
    elif chord_data["difficulty"] == "Intermediate":
        st.warning("🟡 **Build on Basics** - Make sure you master beginner chords first!")
    else:
        st.error("🔴 **Advanced Technique** - This requires solid fundamentals. Don't rush!")
    
    # Save chord
    if st.button("💾 Save to My Favorites", use_container_width=True, type="primary"):
        if "favorite_chords" not in st.session_state:
            st.session_state.favorite_chords = []
        
        if chord_name not in st.session_state.favorite_chords:
            st.session_state.favorite_chords.append(chord_name)
            st.success(f"✅ {chord_name} saved to favorites!")
        else:
            st.info(f"ℹ️ {chord_name} is already in your favorites")

# Favorites section
if "favorite_chords" in st.session_state and st.session_state.favorite_chords:
    st.markdown("---")
    st.subheader("⭐ Your Favorite Chords")
    
    for chord in st.session_state.favorite_chords:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(f"🎸 {chord}", use_container_width=True):
                st.session_state.selected_chord = chord
                st.rerun()
        with col2:
            if st.button("✕", key=f"remove_{chord}"):
                st.session_state.favorite_chords.remove(chord)
                st.rerun()

# Learning guide
st.markdown("---")
st.subheader("📚 Chord Learning Guide")

tab1, tab2, tab3 = st.tabs(["Beginner", "Intermediate", "Advanced"])

with tab1:
    st.write("""
    **Start Here! (Weeks 1-4)**
    
    1. **Week 1-2:** E, A, D, G
    2. **Week 2-3:** Am, Em, Dm
    3. **Week 3-4:** C Major (a bit harder)
    
    **Focus:** Clean sound and basic transitions
    """)

with tab2:
    st.write("""
    **Next Level (Weeks 5-12)**
    
    1. **Week 5-6:** A7, D7, G7
    2. **Week 7-9:** Am7, Dm7, Cmaj7
    3. **Week 10-12:** Start F Major barre chord
    
    **Focus:** Smoother transitions and rhythm control
    """)

with tab3:
    st.write("""
    **Challenge Yourself (Weeks 13+)**
    
    1. Master all barre chords (F, B, etc.)
    2. Learn chord variations and inversions
    3. Understand music theory and progressions
    4. Explore extended chords and jazz voicings
    
    **Focus:** Speed, accuracy, and musical expression
    """)
