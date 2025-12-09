"""
Page: Learning Hub
Tutorials, tips, and structured learning paths
"""

import streamlit as st

st.set_page_config(page_title="Learning Hub", layout="wide")

st.title("📖 Guitar Learning Hub")

# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["🎓 Tutorials", "💡 Tips & Tricks", "📋 Practice Plans", "🎯 Learning Paths"])

with tab1:
    st.subheader("Guitar Technique Tutorials")
    
    techniques = {
        "Barre Chord": "Master the barre chord technique by pressing multiple strings with one finger. Start with F major and practice slowly.",
        "Fingerpicking": "Learn fingerpicking patterns using individual fingers instead of a pick. Great for classical and acoustic styles.",
        "Vibrato": "Add expression by varying the pitch of a note with your finger. Essential for lead guitar.",
        "Slide": "Smooth transitions between notes by sliding your finger along the fretboard.",
        "Hammer-On": "Add dynamics by 'hammering' your finger onto the fretboard to produce a note."
    }
    
    for technique, description in techniques.items():
        with st.expander(f"📚 {technique}"):
            st.write(f"**{description}**")
            if st.button(f"Learn More About {technique}", key=f"learn_{technique}"):
                st.success(f"✅ Here's detailed info about {technique}!")

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
            st.success("✅ Practice Plan Generated!")
            
            plan = [
                {
                    "week": 1,
                    "focus": "Learn basic chord shapes",
                    "practice_minutes": 30,
                    "exercises": ["Chord transitions", "Finger strength"]
                },
                {
                    "week": 2,
                    "focus": "Practice chord changes with rhythm",
                    "practice_minutes": 40,
                    "exercises": ["Metronome practice", "Strumming patterns"]
                },
                {
                    "week": 3,
                    "focus": "Full song playthrough",
                    "practice_minutes": 45,
                    "exercises": ["Tempo increase", "Endurance building"]
                }
            ]
            
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
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Estimated Duration", "8 weeks")
            with col2:
                st.metric("Skills Needed", "3")
            with col3:
                st.metric("Recommended Songs", "5")
            
            st.write("**Prerequisites:**")
            st.write("- Basic open chords")
            st.write("- Rhythm control")
            
            st.write("**Your Learning Path:**")
            for idx, song in enumerate(learning_goal, 1):
                st.write(f"{idx}. {song}")
            
            st.write("**Key Milestones:**")
            st.checkbox("Learn first song")
            st.checkbox("Improve timing")
            st.checkbox("Add dynamics")
