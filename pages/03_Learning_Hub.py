"""
Page: Learning Hub
Tutorials, tips, and structured learning paths
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from utils.ai_advisor import AITabAdvisor
    HAS_AI = True
except:
    HAS_AI = False
    AITabAdvisor = None

st.set_page_config(page_title="Learning Hub", layout="wide")

st.title("📖 Guitar Learning Hub")

# Initialize AI advisor
if HAS_AI and AITabAdvisor:
    if "ai_advisor" not in st.session_state:
        st.session_state.ai_advisor = AITabAdvisor()
    advisor = st.session_state.ai_advisor
else:
    advisor = None

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["🎓 Tutorials", "💡 Tips & Tricks", "📋 Practice Plans", "🎯 Learning Paths"])

with tab1:
    st.subheader("Guitar Technique Tutorials")
    
    techniques = ["Barre Chord", "Fingerpicking", "Vibrato", "Slide", "Hammer-On"]
    
    for technique in techniques:
        with st.expander(f"📚 {technique}"):
            if st.button(f"Learn {technique}", key=f"learn_{technique}"):
                if advisor and advisor.is_configured():
                    with st.spinner(f"Loading tutorial on {technique}..."):
                        explanation = advisor.explain_technique(technique)
                        st.write(explanation)
                else:
                    st.info(f"""
                    📚 **{technique} Tutorial**
                    
                    This is a placeholder. To see AI-powered tutorials with detailed explanations,
                    please add your OpenAI API key in **Settings**.
                    
                    **Basic Info:**
                    - Difficulty: Intermediate
                    - Time to Learn: 2-4 weeks
                    - Benefits: Unlock many songs
                    """)

with tab2:
    st.subheader("💡 Tips & Tricks")
    
    tips = [
        {
            "title": "Improve Chord Transitions",
            "content": "Practice moving between two chords slowly, focusing on accuracy over speed. Gradually increase tempo as muscle memory develops."
        },
        {
            "title": "Build Finger Strength",
            "content": "Use exercises like finger taps and stretches. Practice 15 minutes daily for best results."
        },
        {
            "title": "Develop Rhythm",
            "content": "Use a metronome starting at 60 BPM and gradually increase. Practice with different strumming patterns."
        },
        {
            "title": "Prevent Hand Fatigue",
            "content": "Take breaks every 30 minutes. Use proper posture and hand positioning."
        }
    ]
    
    for tip in tips:
        with st.expander(f"💡 {tip['title']}"):
            st.write(tip['content'])

with tab3:
    st.subheader("📋 Personalized Practice Plans")
    
    col1, col2 = st.columns(2)
    
    with col1:
        song_name = st.text_input("Song Name", placeholder="e.g., Wonderwall")
        artist_name = st.text_input("Artist", placeholder="e.g., Oasis")
    
    with col2:
        current_level = st.selectbox("Current Level", ["Beginner", "Intermediate", "Advanced"])
        goal_level = st.selectbox("Goal Level", ["Beginner", "Intermediate", "Advanced"])
    
    hours_per_week = st.slider("Hours Available Per Week", 1, 20, 5)
    
    if st.button("Generate Practice Plan"):
        if not song_name or not artist_name:
            st.warning("Please enter a song name and artist!")
        else:
            if advisor and advisor.is_configured():
                with st.spinner("Creating your personalized plan..."):
                    plan_text = advisor.generate_practice_plan(
                        song_name, artist_name, current_level, goal_level, hours_per_week
                    )
                    st.success("✅ Practice Plan Generated!")
                    st.write(plan_text)
            else:
                st.success("✅ Practice Plan Generated!")
                st.write(f"""
                **4-Week Practice Plan for "{song_name}" by {artist_name}**
                
                **Week 1: Learn basic chord shapes**
                - Daily practice: 30 minutes
                - Focus: Chord transitions
                - Exercises: Finger strength building
                
                **Week 2: Practice chord changes with rhythm**
                - Daily practice: 40 minutes
                - Focus: Metronome practice
                - Exercises: Strumming patterns
                
                **Week 3: Full song playthrough**
                - Daily practice: 45 minutes
                - Focus: Tempo increase
                - Exercises: Endurance building
                
                **Week 4: Master and perform**
                - Daily practice: 50 minutes
                - Focus: Dynamics and expression
                - Exercises: Performance practice
                
                *To get AI-customized plans based on your specific goals, add your OpenAI API key in Settings!*
                """)

with tab4:
    st.subheader("🎯 Learning Paths")
    
    learning_goal = st.multiselect(
        "What songs would you like to learn?",
        [
            "Wonderwall - Oasis",
            "Stairway to Heaven - Led Zeppelin",
            "Hotel California - Eagles",
            "Comfortably Numb - Pink Floyd",
            "Cliffs of Dover - Eric Johnson"
        ]
    )
    
    if learning_goal and st.button("Create Learning Path"):
        if advisor and advisor.is_configured():
            with st.spinner("Building your learning path..."):
                path_text = advisor.get_learning_path(learning_goal)
                st.write(path_text)
        else:
            with st.spinner("Building your learning path..."):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Estimated Duration", "8-12 weeks")
                with col2:
                    st.metric("Skills Needed", "3")
                with col3:
                    st.metric("Recommended Songs", len(learning_goal))
                
                st.write("**Prerequisites:**")
                st.write("- Basic open chords (Am, C, G, D, E)")
                st.write("- Basic rhythm and timing")
                st.write("- Finger dexterity exercises")
                
                st.write("**Your Learning Path:**")
                for idx, song in enumerate(learning_goal, 1):
                    st.write(f"{idx}. {song}")
                
                st.write("**Key Milestones:**")
                st.checkbox("Learn first song")
                st.checkbox("Improve timing")
                st.checkbox("Add dynamics")
                
                st.info("*For a personalized learning path, add your OpenAI API key in Settings!*")
