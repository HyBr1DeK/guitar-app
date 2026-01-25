# 🎸 Guitar Tab Finder AI

A Streamlit-based application that uses AI to help guitarists find accurate tabs for any song, learn techniques, and track their progress.

## ✨ Features

### Main Features
- **🔍 Intelligent Tab Search**: Search for guitar tabs by song name and artist
- **🤖 AI Assistant**: Chat with an AI-powered guitar expert for recommendations and guidance
- **📚 Personal Library**: Save and organize your favorite tabs and learning progress
- **📖 Learning Hub**: Access tutorials, practice plans, and structured learning paths
- **⚙️ Customizable Settings**: Configure preferences, API keys, and notification settings

### Smart Capabilities
- **Tab Difficulty Filtering**: Filter tabs by skill level (Beginner, Intermediate, Advanced)
- **Source Selection**: Search across multiple tab sources (Ultimate Guitar, Chordify, etc.)
- **Key Transposition**: Automatically transpose tabs to your preferred key
- **Practice Plans**: AI-generated personalized practice schedules
- **Learning Paths**: Structured pathways to master multiple songs
- **Chord Analysis**: Understand chord progressions and music theory

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Guitar-app.git
cd Guitar-app
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Editor / Pylance setup (VS Code)

If you're using VS Code and see warnings like "Import 'streamlit' could not be resolved":
- Make sure you've selected the correct Python interpreter (your virtualenv) in VS Code.
- Install dependencies in that environment (`pip install -r requirements.txt`).
- This repository includes an editor-only stub for Streamlit to help Pylance type-checking without installing packages; if you're still seeing issues, reload VS Code or re-select the interpreter.

If Pylance is still unresolved, try reloading the window (`Developer: Reload Window`) or re-creating the venv.

## 📁 Project Structure

```
Guitar-app/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── utils/
│   ├── tab_finder.py     # Tab searching and retrieval logic
│   └── ai_advisor.py     # AI integration and recommendations
└── pages/
    ├── 01_AI_Assistant.py      # Chat interface with AI
    ├── 02_My_Library.py        # Personal tab collection
    ├── 03_Learning_Hub.py      # Tutorials and practice plans
    └── 04_Settings.py          # User preferences and API configuration
```

## 🎯 Usage Guide

### Finding Tabs
1. Enter a song name and artist on the main page (e.g., "Wonderwall by Oasis")
2. View results from multiple sources with difficulty ratings
3. Click on a tab to view details and chords
4. Save tabs to your library

### Using AI Assistant
1. Go to the "AI Assistant" page
2. Ask questions about:
   - Song recommendations for your skill level
   - Guitar techniques and how to practice them
   - Practice plans for specific songs
   - Music theory and chord progressions

### Building a Practice Plan
1. Navigate to "Learning Hub" → "Practice Plans"
2. Select a song and your current/goal skill level
3. Specify available practice hours per week
4. Receive a week-by-week breakdown with specific exercises

### Tracking Progress
1. Visit "My Library" to organize your tabs
2. Add songs you're currently learning
3. Track progress with the progress slider
4. Mark songs as "Mastered" when complete
5. View statistics on your dashboard

## 🔧 Configuration

### API Keys Setup
1. Get an **OpenAI API key** from https://platform.openai.com/api-keys
2. Go to Settings → API Keys
3. Paste your OpenAI key (keep it private!)
4. Optionally add Ultimate Guitar API key for enhanced searching

### Preferences
Configure in Settings:
- **Skill Level**: Beginner, Intermediate, Advanced, Professional
- **Guitar Types**: Acoustic, Electric, Classical, Bass
- **Preferred Tuning**: Standard, Drop D, Open G, etc.
- **Tab Sources**: Choose where to search for tabs
- **Notifications**: Enable/disable notifications and set frequency

## 🎓 Learning Resources

### Included Tutorials
- Barre Chords
- Fingerpicking Patterns
- Vibrato Technique
- Slides
- Hammer-On Techniques

### Practice Tips
- Chord transition exercises
- Finger strength building
- Rhythm development
- Hand fatigue prevention

## 🤝 Integration Points

The app is designed to integrate with:
- **OpenAI GPT API** for intelligent recommendations
- **Ultimate Guitar API** for tab searching
- **Chordify** for automatic chord detection
- Local caching for improved performance

## 🛣️ Roadmap

### Phase 1 (Current)
- ✅ Basic tab searching
- ✅ Tab organization and library
- ✅ Learning hub structure
- ✅ Settings configuration

### Phase 2 (Planned)
- 🔄 Full OpenAI integration
- 🔄 Real API connections for tab sources
- 🔄 Video tutorials
- 🔄 BPM-adjustable playback

### Phase 3 (Future)
- 🔜 Gamification and achievements
- 🔜 Community features and sharing
- 🔜 Mobile app version
- 🔜 Offline mode

## 💡 Tips for Best Results

1. **Start Simple**: Begin with beginner-level songs
2. **Consistent Practice**: Use the generated practice plans
3. **Use Metronome**: Practice with a metronome for rhythm
4. **Ask AI**: Use the AI Assistant for personalized guidance
5. **Track Progress**: Update your library regularly
6. **Take Breaks**: Avoid hand fatigue with scheduled breaks

## 📝 Notes

- Tabs are fetched from public sources
- Always respect copyright and licensing terms
- Practice consistently for best results
- AI recommendations are suggestions - adjust based on your comfort level

## 🆘 Troubleshooting

**App won't start?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try clearing browser cache and refreshing

**API connection errors?**
- Check your internet connection
- Verify API keys are correct in Settings
- Check if tab sources are online

**Performance issues?**
- Clear cache in Settings
- Reduce number of displayed results
- Try limiting to specific tab sources

## 📧 Support

For issues, feature requests, or suggestions, please:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🎵 Credits

- Built with [Streamlit](https://streamlit.io/)
- AI powered by [OpenAI](https://openai.com/)
- Tab data from multiple public sources

---

**Happy Playing! 🎸**

*Last Updated: November 25, 2025*
