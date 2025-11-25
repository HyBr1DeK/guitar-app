"""
Page: Learning Hub
Tutorials, tips, and structured learning paths
"""

import streamlit as st
from utils.ai_advisor import AITabAdvisor

st.set_page_config(page_title="Learning Hub", layout="wide")

st.title("📖 Guitar Learning Hub")

# Initialize advisor
ai_advisor = AITabAdvisor()

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["🎓 Tutorials", "💡 Tips & Tricks", "📋 Practice Plans", "🎯 Learning Paths"])

with tab1:
    st.subheader("Guitar Technique Tutorials")
    
    techniques = [
        ("Barre Chord", "Master the barre chord technique"),
        ("Fingerpicking", "Learn fingerpicking patterns"),
        ("Vibrato", "Add expression with vibrato"),
        ("Slide", "Smooth transitions between notes"),
        ("Hammer-On", "Add dynamics to your playing")
    ]
    
    for technique, description in techniques:
        with st.expander(f"📚 {technique}"):
            st.write(f"**{description}**")
            
            if st.button(f"Learn {technique}", key=f"learn_{technique}"):
                explanation = ai_advisor.explain_technique(technique)
                st.success(explanation)

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
        song_name = st.text_input("Song Name")
        artist_name = st.text_input("Artist")
    
    with col2:
        current_level = st.selectbox("Current Level", ["Beginner", "Intermediate", "Advanced"])
        goal_level = st.selectbox("Goal Level", ["Beginner", "Intermediate", "Advanced"])
    
    hours_per_week = st.slider("Hours Available Per Week", 1, 20, 5)
    
    if st.button("Generate Practice Plan"):
        with st.spinner("Creating your personalized plan..."):
            plan = ai_advisor.generate_practice_plan(
                song_name or "Sample Song",
                artist_name or "Sample Artist",
                current_level,
                goal_level,
                hours_per_week
            )
            
            st.success("✅ Practice Plan Generated!")
            for week in plan:
                with st.expander(f"Week {week['week']}: {week['focus']}"):
                    st.write(f"**Daily Practice:** {week['practice_minutes']} minutes")
                    st.write("**Exercises:**")
                    for exercise in week['exercises']:
                        st.write(f"- {exercise}")

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
        with st.spinner("Building your learning path..."):
            path = ai_advisor.get_learning_path(learning_goal)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Estimated Duration", f"{path['estimated_weeks']} weeks")
            with col2:
                st.metric("Skills Needed", len(path['prerequisite_skills']))
            with col3:
                st.metric("Recommended Songs", len(path['recommended_songs']))
            
            st.write("**Prerequisites:**")
            for skill in path['prerequisite_skills']:
                st.write(f"- {skill}")
            
            st.write("**Your Learning Path:**")
            for idx, song in enumerate(path['recommended_songs'], 1):
                st.write(f"{idx}. {song}")
            
            st.write("**Key Milestones:**")
            for milestone in path['milestones']:
                st.checkbox(milestone)
