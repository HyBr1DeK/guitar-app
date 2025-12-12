"""
Page: Settings & Preferences
User configuration and API setup
"""

import streamlit as st
import os

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
    
    st.info("""
    **🚀 Enable AI Features!**
    
    To use AI-powered recommendations, explanations, and practice plans, 
    you need an OpenAI API key.
    """)
    
    st.markdown("**Step 1: Get Your API Key**")
    st.write("""
    1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
    2. Sign up or log in with your OpenAI account
    3. Click "Create new secret key"
    4. Copy the key (you won't see it again!)
    """)
    
    st.markdown("**Step 2: Add Your Key Here**")
    
    # Get current API key if it exists
    current_key = st.secrets.get("OPENAI_API_KEY", "")
    
    openai_key = st.text_input(
        "OpenAI API Key",
        value=current_key,
        type="password",
        help="Paste your OpenAI API key here. It will be stored securely."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Save API Key", type="primary"):
            if openai_key:
                try:
                    # For Streamlit Cloud, users need to add it through Secrets
                    st.success("""
                    ✅ **To complete setup:**
                    
                    Since you're on Streamlit Cloud, please:
                    1. Click "Deploy" or go to your app settings
                    2. Click "Secrets" in the sidebar
                    3. Add: `OPENAI_API_KEY = "your-key-here"`
                    4. Rerun the app
                    
                    For local development, create a `.streamlit/secrets.toml` file:
                    ```
                    OPENAI_API_KEY = "your-key-here"
                    ```
                    """)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please paste your API key first!")
    
    with col2:
        if st.button("Test Connection"):
            if openai_key or current_key:
                with st.spinner("Testing connection..."):
                    try:
                        # Simple test - try to import and create client
                        from openai import OpenAI
                        test_client = OpenAI(api_key=openai_key or current_key)
                        
                        # Try a simple API call
                        response = test_client.models.list()
                        st.success("✅ Connection successful! Your API key is valid.")
                    except Exception as e:
                        st.error(f"❌ Connection failed: {str(e)}")
            else:
                st.warning("Please add your API key first!")
    
    st.warning("""
    ⚠️ **Security Note:**
    - Never share your API key publicly
    - On Streamlit Cloud, keys are stored securely and never shown in logs
    - You'll be charged by OpenAI only for what you use
    """)

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
        st.cache_data.clear()
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
            }
            st.success("✅ Settings reset to defaults!")
