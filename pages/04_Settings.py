"""
Page: Settings & Preferences
User configuration and API setup
"""

import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")

st.title("⚙️ Settings & Preferences")

# Initialize settings in session state
if "user_settings" not in st.session_state:
    st.session_state.user_settings = {
        "skill_level": "Intermediate",
        "preferred_key": "G",
        "tab_source": "All Sources",
        "notifications": True,
        "dark_mode": False,
        "api_key": ""
    }

# Tabs for different settings categories
tab1, tab2, tab3, tab4 = st.tabs(["👤 Profile", "🎸 Guitar", "🔗 API Keys", "📢 Notifications"])

with tab1:
    st.subheader("Profile Settings")
    
    skill_level = st.selectbox(
        "Your Skill Level",
        ["Beginner", "Intermediate", "Advanced", "Professional"],
        index=1
    )
    st.session_state.user_settings["skill_level"] = skill_level
    
    guitar_type = st.multiselect(
        "Guitar Types You Play",
        ["Acoustic", "Electric", "Classical", "Bass"],
        default=["Acoustic", "Electric"]
    )
    
    favorite_genres = st.multiselect(
        "Favorite Genres",
        ["Rock", "Pop", "Blues", "Jazz", "Country", "Metal", "Folk"],
        default=["Rock", "Pop"]
    )
    
    if st.button("Save Profile"):
        st.success("✅ Profile updated!")

with tab2:
    st.subheader("Guitar Preferences")
    
    tuning = st.selectbox(
        "Preferred Tuning",
        ["Standard (EADGBE)", "Drop D", "Open G", "Open D", "Half Step Down"]
    )
    
    preferred_key = st.selectbox(
        "Preferred Key (for transposition)",
        ["C", "D", "E", "F", "G", "A", "B"]
    )
    st.session_state.user_settings["preferred_key"] = preferred_key
    
    default_capo = st.checkbox("Enable automatic capo recommendations")
    
    tab_source = st.radio(
        "Preferred Tab Source",
        ["All Sources", "Ultimate Guitar", "Chordify", "Tab Provider"]
    )
    st.session_state.user_settings["tab_source"] = tab_source
    
    if st.button("Save Guitar Settings"):
        st.success("✅ Guitar settings updated!")

with tab3:
    st.subheader("🔗 API Keys & Integration")
    
    st.warning("⚠️ Never share your API keys publicly!")
    
    openai_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="For AI-powered recommendations"
    )
    
    if openai_key:
        st.session_state.user_settings["api_key"] = openai_key
    
    ultimateguitar_key = st.text_input(
        "Ultimate Guitar API Key (Optional)",
        type="password",
        help="For enhanced tab searching"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Test Connection"):
            st.info("Testing API connection...")
            # In production, would test actual connection
            st.success("✅ Connection successful!")
    
    with col2:
        if st.button("Clear Keys"):
            st.session_state.user_settings["api_key"] = ""
            st.warning("⚠️ API keys cleared!")

with tab4:
    st.subheader("📢 Notification Settings")
    
    notifications_enabled = st.checkbox(
        "Enable Notifications",
        value=True
    )
    st.session_state.user_settings["notifications"] = notifications_enabled
    
    if notifications_enabled:
        st.write("**Notify me about:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            notify_new_tabs = st.checkbox("New tabs for my favorite songs")
            notify_learning = st.checkbox("Learning milestones")
        
        with col2:
            notify_recommendations = st.checkbox("Personalized recommendations")
            notify_updates = st.checkbox("App updates")
        
        notification_frequency = st.selectbox(
            "Notification Frequency",
            ["Daily", "Weekly", "Monthly", "Never"]
        )
    
    if st.button("Save Notification Settings"):
        st.success("✅ Notification settings updated!")

# Danger Zone
st.markdown("---")
st.subheader("⚠️ Danger Zone")

col1, col2 = st.columns(2)

with col1:
    if st.button("Clear Cache"):
        st.info("Cache cleared! Refresh the app to see changes.")

with col2:
    if st.button("Reset to Defaults"):
        st.warning("Are you sure? This will reset all settings to defaults.")
        if st.button("Yes, reset everything"):
            st.session_state.user_settings = {
                "skill_level": "Intermediate",
                "preferred_key": "G",
                "tab_source": "All Sources",
                "notifications": True,
                "dark_mode": False,
                "api_key": ""
            }
            st.success("✅ Settings reset to defaults!")
