"""
AI Integration Module
Handles guitar questions and provides intelligent responses
"""

import os
from typing import Optional
import re

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

class AITabAdvisor:
    """AI-powered advisor for guitar tabs and learning"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = None
        self.model = "gpt-3.5-turbo"
        
        # Try to initialize OpenAI if API key is available
        if self.api_key and HAS_OPENAI:
            try:
                self.client = OpenAI(api_key=self.api_key)
            except Exception as e:
                print(f"OpenAI initialization note: {e}")
    
    def is_configured(self):
        """Check if OpenAI is properly configured"""
        return self.client is not None
    
    def chat(self, message: str, system_prompt: str = None) -> str:
        """
        Get AI response - uses OpenAI API if available, otherwise uses rule-based responses
        
        Args:
            message: User's question or request
            system_prompt: Optional system prompt for context
            
        Returns:
            AI-generated response
        """
        # Try to use OpenAI first if configured
        if self.client:
            try:
                return self._openai_chat(message, system_prompt)
            except Exception as e:
                print(f"OpenAI error: {e}")
                # Fall back to rule-based responses
                return self._rule_based_response(message)
        else:
            # Use rule-based responses
            return self._rule_based_response(message)
    
    def _openai_chat(self, message: str, system_prompt: str = None) -> str:
        """Use OpenAI API for responses"""
        system_msg = system_prompt or """You are an expert guitar teacher and tab finder AI. 
You help guitarists find tabs, learn techniques, and improve their playing. 
Be concise, friendly, and provide practical advice. When asked about songs, 
suggest beginner-friendly options or provide learning tips. Use examples when helpful."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        return response.choices[0].message.content
    
    def _rule_based_response(self, message: str) -> str:
        """Intelligent rule-based responses for common guitar questions"""
        msg_lower = message.lower()
        
        # F chord questions
        if any(word in msg_lower for word in ["f chord", "f major", "how to make f"]):
            return """🎸 **How to Play an F Major Chord**

The F major chord is a barre chord - one of the first challenges for many guitarists. Here's how to play it:

**Step 1: Position Your Finger**
- Place your index finger across all 6 strings at the 1st fret (this is called a "barre")
- Press down firmly - this is the hardest part!

**Step 2: Add Your Other Fingers**
- Middle finger on the 2nd fret of the A string (5th string)
- Ring finger on the 3rd fret of the D string (4th string)  
- Pinky on the 3rd fret of the high E string (1st string)

**Step 3: Strum**
- Start from the A string (5th string), not the low E
- Strum down with a smooth motion

**Pro Tips:**
✓ Your barre finger should be close to the fret (but not ON it)
✓ Press hard - barre chords need firm pressure
✓ Practice building up finger strength gradually
✓ Start slowly and increase speed as you get comfortable

**Practice Method:**
- Hold the chord for 10 seconds, rest 5 seconds, repeat
- Do this daily for 2-3 weeks to build muscle memory
- Once comfortable, practice switching between F and C major chords

**Why F Chord Matters:**
The F major chord appears in hundreds of songs and builds finger strength for other barre chords. Once you master it, you'll unlock many new songs!"""
        
        # Barre chord questions
        elif any(word in msg_lower for word in ["barre chord", "how to play barre", "struggling with barre"]):
            return """🎸 **Mastering Barre Chords**

Barre chords can be challenging, but with the right approach, you'll get there! Here's the complete guide:

**What is a Barre Chord?**
A barre chord uses one finger (usually your index finger) to press multiple strings at the same fret simultaneously.

**Essential Steps:**

1. **Hand Position**
   - Keep your thumb behind the neck, roughly aligned with your middle finger
   - Your wrist should be relatively straight (not bent too much)
   - Index finger should be firm but not rigid

2. **Building Strength**
   - Barre chords require finger strength that develops over time
   - Practice 15-20 minutes daily to build muscle
   - Use hand stretches to prevent fatigue

3. **Common Barre Chords to Master:**
   - F Major (1st fret) - Most challenging
   - B Minor (2nd fret) - Great progression
   - Bm (2nd fret variation)
   - Any major/minor at higher frets

4. **Training Plan:**
   - Week 1-2: Hold each chord for 10 seconds, rest, repeat
   - Week 3-4: Switch between barre chords and open chords
   - Week 5+: Use them in songs and chord progressions

**Troubleshooting:**
- **Muted strings?** Press harder and position closer to the fret
- **Hand fatigue?** Take breaks, do stretches, build strength gradually
- **Can't switch fast?** Practice the specific transition slowly first

**Songs to Practice:**
- "Wonderwall" by Oasis
- "Brown Eyed Girl" by Van Morrison
- "Wild Thing" by The Troggs

With consistent practice, most guitarists master barre chords in 4-8 weeks!"""
        
        # Fingerpicking questions
        elif any(word in msg_lower for word in ["fingerpicking", "finger picking", "fingerstyle", "how to fingerpick"]):
            return """🎸 **Fingerpicking: Complete Beginner's Guide**

Fingerpicking adds a beautiful, dynamic quality to your playing. Here's how to start:

**Basic Hand Position:**
- Thumb plays the bass strings (E, A, D)
- Index finger plays the G string
- Middle finger plays the B string
- Ring finger plays the high E string
- Use your nails or fingernails for better tone

**Simple Fingerpicking Pattern (Folk Style):**
```
Thumb: E string (low)
Index: G string
Middle: B string
Ring: E string (high)
Middle: B string
Index: G string
```
Practice this pattern slowly, about 60 BPM, until it becomes muscle memory.

**Step-by-Step Learning:**
1. **Week 1:** Nail down the basic pattern at slow speed
2. **Week 2:** Increase tempo gradually (use a metronome)
3. **Week 3:** Apply it to actual chords
4. **Week 4+:** Learn variations and apply to songs

**Famous Fingerpicking Patterns:**
- Travis Picking (Country style)
- Classical fingerpicking
- Arpeggios (playing each note separately)

**Best Songs to Learn:**
- "Landslide" by Fleetwood Mac
- "Blackbird" by The Beatles
- "Tears in Heaven" by Eric Clapton
- "Pink Floyd" style - various songs

**Practice Tips:**
✓ Start slow (40-60 BPM) with accuracy as priority
✓ Use a metronome to develop rhythm
✓ Build up speed gradually, not suddenly
✓ Practice daily even if just for 15 minutes

Fingerpicking takes 3-6 weeks to feel comfortable. Be patient and consistent!"""
        
        # Chord progression questions
        elif any(word in msg_lower for word in ["chord progression", "chord change", "switch between chords"]):
            return """🎸 **Master Chord Progressions & Transitions**

Smooth chord transitions are crucial for playing songs. Here's your complete guide:

**Why Chord Transitions Matter:**
- Separates beginners from intermediate players
- Allows you to play full songs smoothly
- Builds finger muscle memory
- Develops rhythm consistency

**Top Chord Progressions to Learn:**

**1. I - IV - V - I (Most Popular)**
Examples: G - C - D - G or C - F - G - C
- Used in countless songs
- Great for practicing transitions

**2. I - V - vi - IV**
Example: C - G - Am - F
- Modern pop favorite
- Emotional and versatile

**3. vi - IV - I - V**
Example: Am - F - C - G
- Sad/melancholic feel
- Very popular in modern music

**Practice Method for Smooth Transitions:**

**Stage 1: Slow Practice (30 BPM)**
- Play each chord clearly
- Focus on accuracy over speed
- Hold each chord for 2 seconds

**Stage 2: Increase Tempo (60 BPM)**
- Gradually increase tempo
- Maintain accuracy

**Stage 3: Song Application (Full Tempo)**
- Apply to real songs
- Build confidence

**Specific Exercises:**

1. **Two-Chord Drill**
   - Pick C and G chords
   - Switch between them 10 times slowly
   - Increase speed gradually

2. **Progressive Practice**
   - Add a new chord only when previous transition is smooth
   - Focus on one transition at a time

3. **Metronome Training**
   - Start at 40 BPM
   - Increase by 10 BPM weekly
   - Target: Full song tempo

**Timeline:**
- Week 1-2: Basic transitions (2-3 chords)
- Week 3-4: Full progressions
- Week 5+: Smooth, fast transitions

**Common Mistakes to Avoid:**
❌ Rushing the learning process
❌ Not using a metronome
❌ Irregular practice sessions
❌ Not holding chords long enough

With daily 20-30 minute practice, you'll master chord transitions in 4-6 weeks!"""
        
        # Technique questions
        elif any(word in msg_lower for word in ["vibrato", "hammer on", "pull off", "slide", "technique"]):
            return """🎸 **Advanced Guitar Techniques Explained**

Let me break down the major guitar techniques to take your playing to the next level!

**1. VIBRATO**
A technique where you subtly change the pitch by bending the string back and forth.

*How to Play:*
- Fret a note
- Bend the string up slightly
- Bend it back down smoothly
- Repeat at a steady rhythm

*Practice:*
- Start on a single string (high E)
- Practice the motion slowly
- Aim for consistent speed and width

**2. HAMMER-ON**
Playing a second note by "hammering" your finger onto the fretboard.

*How to Play:*
- Pick a note (e.g., 5th fret)
- Without picking again, "hammer" your next finger onto a higher fret
- The second note should ring out clearly

*Example:* Open E string → hammer onto 2nd fret → E to F#

**3. PULL-OFF**
The opposite of hammer-on - release a finger to play a lower note.

*How to Play:*
- Fret two notes (e.g., 2nd and 5th frets)
- Pick the higher note
- Quickly pull your finger off to play the lower note
- The lower note should ring out

**4. SLIDE**
Smoothly transition between two notes by sliding your finger along the fretboard.

*How to Play:*
- Fret a note and pick it
- Slide your finger to the next fret/note
- Keep pressure on the string throughout

*Used in:* Blues, rock, country music

**5. BENDING**
Change the pitch of a note by pushing/pulling the string.

*How to Play:*
- Fret a note
- Push the string up (or pull down) to raise the pitch
- Quarter bend (0.5 steps), half bend (1 step), or full bend (2 steps)

**Learning Order:**
1. Start with hammer-on and pull-off
2. Add slides
3. Practice bending
4. Master vibrato (most difficult)

**Timeline:**
- 1-2 weeks: Basic hammer-on and pull-off
- 3-4 weeks: Confident with all techniques
- 5+ weeks: Smooth and musical application

Begin by practicing each technique for 5-10 minutes daily on a single string!"""
        
        # Beginner questions
        elif any(word in msg_lower for word in ["beginner", "start", "easy song", "first song"]):
            return """🎸 **Perfect Songs to Start With**

As a beginner, you want songs that are:
- Simple chord progressions
- Slow tempo
- Few chord changes
- Fun and motivating!

**Top 5 Beginner Songs:**

**1. "Wonderwall" by Oasis** ⭐
- Chords: Em7, Cadd9 (2 chords!)
- Why: Super simple, very motivating
- Time to learn: 1-2 weeks

**2. "Three Little Birds" by Bob Marley**
- Chords: A, E, B (basic major chords)
- Why: Upbeat, feel-good vibe
- Time to learn: 2-3 weeks

**3. "Knockin' On Heaven's Door" by Bob Dylan**
- Chords: G, D, A, D (simple progression)
- Why: Classic, straightforward
- Time to learn: 2-3 weeks

**4. "Horse With No Name" by America**
- Chords: Em - Asus4 (repeated pattern)
- Why: Minimal changes, easy rhythm
- Time to learn: 1-2 weeks

**5. "Brown Eyed Girl" by Van Morrison**
- Chords: G, D, A (standard progression)
- Why: Fun, upbeat, satisfying
- Time to learn: 3-4 weeks

**Learning Strategy:**
- Weeks 1-2: Learn 2-3 basic open chords (G, D, A, C)
- Weeks 3-4: Practice transitioning smoothly
- Weeks 5-6: Pick your first song and master it
- Week 7+: Learn additional songs

**Pro Tips:**
✓ Don't rush - play songs slowly first
✓ Use a capo for easier versions
✓ Practice chord changes most
✓ Celebrate small wins!

**Next Steps:**
1. Learn Em, Am, C, G chords first
2. Practice switching between 2 chords
3. Pick "Wonderwall" as your first song
4. Enjoy the journey!

Most beginners can play their first full song in 4-8 weeks with consistent practice!"""
        
        # General guitar help
        elif any(word in msg_lower for word in ["help", "how to", "problem", "issue", "stuck"]):
            return """🎸 **Guitar Help & Troubleshooting**

I'm here to help! Here are common issues and solutions:

**Issue: Fingers hurt when playing**
- **Solution:** This is normal for beginners! Your fingertips will develop calluses in 2-3 weeks
- Take breaks every 20-30 minutes
- Practice 30 minutes daily rather than 3 hours once a week

**Issue: Chords sound muted or buzzing**
- **Solution:** Press harder on the strings
- Keep fingers as close to the frets as possible
- Curve your fingers more (arch your hand)

**Issue: Can't switch chords fast enough**
- **Solution:** Slow down! Accuracy comes before speed
- Use a metronome starting at 40 BPM
- Practice one transition at a time

**Issue: Strings hurt my wrist**
- **Solution:** Check your wrist position - it should be mostly straight
- Don't bend your wrist too much
- Take breaks if it hurts (not just uncomfortable)

**Issue: Can't play barre chords**
- **Solution:** This takes 4-8 weeks of practice
- Build finger strength gradually
- Don't give up - everyone struggles with these!

**Issue: Can't keep rhythm**
- **Solution:** Use a metronome app (MetronomeBot, Tempo)
- Start very slow (40 BPM)
- Focus on consistent strumming

**General Tips:**
✓ Practice daily (even 20 minutes helps)
✓ Use a metronome
✓ Practice slowly before fast
✓ Take breaks to avoid injury
✓ Be patient - guitar takes time!

**What specific issue are you facing?** Tell me more details and I can give more targeted advice!"""
        
        # Default helpful response
        else:
            return """🎸 **Guitar Learning Assistant**

Great question! I can help you with:

**🎵 Song Learning:**
- Easy beginner songs to start with
- Specific songs you want to learn
- Chord progressions and tips

**🎸 Techniques:**
- How to play specific chords (F, Bm, etc.)
- Fingerpicking, barre chords, vibrato, hammer-ons
- Strumming patterns and rhythm

**📚 Practice Plans:**
- Creating personalized practice routines
- Building finger strength
- Improving chord transitions

**🎯 General Help:**
- Troubleshooting playing issues
- Overcoming common problems
- Progress tracking

**Examples of questions I can answer:**
- "How do I play an F chord?"
- "What's a good beginner song?"
- "How do I improve my barre chords?"
- "What techniques should I learn?"
- "My fingers hurt, what should I do?"

**Just ask me anything about guitar!** I'm here to help you improve! 🎸"""
    
    def get_tab_recommendation(self, skill_level: str, genre: str = "rock") -> str:
        """Get song recommendations based on skill level and genre"""
        prompt = f"""Recommend 3-4 guitar songs for someone with {skill_level} skill level 
interested in {genre} music. For each song, briefly explain:
1. Song name and artist
2. Why it's good for their level
3. Key techniques they'll learn
Keep it concise and practical."""
        
        return self.chat(prompt)
    
    def analyze_chord_progression(self, chords: list) -> str:
        """Analyze a chord progression"""
        chord_str = ", ".join(chords)
        prompt = f"""Analyze this chord progression: {chord_str}
Explain:
1. The likely key
2. The emotional mood
3. Techniques needed to play it
4. Similar famous songs that use this progression
Keep it educational but concise."""
        
        return self.chat(prompt)
    
    def generate_practice_plan(self, song: str, artist: str, current_level: str, 
                               goal_level: str, hours_per_week: int) -> str:
        """Generate a personalized practice plan"""
        prompt = f"""Create a 4-week practice plan for learning "{song}" by {artist}.
Current skill level: {current_level}
Goal skill level: {goal_level}
Available practice time: {hours_per_week} hours per week

Format as:
Week 1: [focus area]
- Daily exercises
- Time allocation

Week 2: [focus area]
...and so on.

Be specific and practical."""
        
        return self.chat(prompt)
    
    def explain_technique(self, technique: str) -> str:
        """Explain a guitar technique in detail"""
        prompt = f"""Explain the "{technique}" guitar technique in a way that's easy to understand.
Include:
1. Basic definition
2. Step-by-step instructions
3. Common mistakes to avoid
4. Practice tips
5. Songs that use this technique
Keep it concise and practical for beginners."""
        
        return self.chat(prompt)
    
    def get_learning_path(self, songs: list) -> str:
        """Create a learning path for multiple songs"""
        song_list = ", ".join(songs)
        prompt = f"""Create a learning path for mastering these songs: {song_list}
Include:
1. Recommended order to learn them
2. Prerequisite skills needed
3. Estimated timeline
4. Key techniques to focus on
5. Practice structure"""
        
        return self.chat(prompt)
