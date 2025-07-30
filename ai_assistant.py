#!/usr/bin/env python3
"""
AI Assistant - Prompt Engineering Project
A comprehensive AI Assistant that demonstrates different prompt engineering techniques
"""

import os
import time
import json
from datetime import datetime

class AIAssistant:
    def __init__(self):
        self.stats = {
            'total_queries': 0,
            'helpful_responses': 0,
            'not_helpful_responses': 0,
            'function_usage': {
                'questions': 0,
                'summarize': 0,
                'creative': 0,
                'advice': 0
            }
        }
        
        self.sample_prompts = {
            'questions': [
                "What is the capital of France?",
                "Can you explain the historical significance of the Eiffel Tower in Paris?",
                "Compare the educational systems of France and Germany in 5 key points."
            ],
            'summarize': [
                "Summarize the following article in 3 lines: [Insert your text here]",
                "Extract and list the 5 main points from this passage: [Insert your text here]",
                "Provide a summary focusing only on challenges and recommendations: [Insert your text here]"
            ],
            'creative': [
                "Write a short story about a dragon who learns to live peacefully with humans.",
                "Compose a four-line poem about the beauty of autumn evenings.",
                "Suggest 3 unique science fiction novel plots involving space exploration and AI."
            ],
            'advice': [
                "Give me 5 effective study tips for preparing for exams.",
                "Suggest ways to stay motivated while working on long projects.",
                "Provide daily routines that can improve mental health and productivity."
            ]
        }
        
        self.load_stats()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print the application header"""
        print("=" * 60)
        print("🤖 AI ASSISTANT - PROMPT ENGINEERING PROJECT")
        print("=" * 60)
        print("Your Intelligent Prompt Engineering Companion")
        print("=" * 60)

    def print_menu(self):
        """Print the main menu"""
        print("\n📋 AVAILABLE FUNCTIONS:")
        print("1. ❓ Answer Questions")
        print("2. 📝 Summarize Text") 
        print("3. 🎨 Generate Creative Content")
        print("4. 💡 Provide Advice")
        print("5. 📊 View Statistics")
        print("6. 🚪 Exit")
        print("-" * 40)

    def show_sample_prompts(self, function_type):
        """Display sample prompts for the selected function"""
        print(f"\n💫 SAMPLE PROMPTS FOR {function_type.upper()}:")
        print("-" * 40)
        for i, prompt in enumerate(self.sample_prompts[function_type], 1):
            print(f"{i}. {prompt}")
        print("-" * 40)

    def get_user_input(self, prompt="Enter your message: "):
        """Get user input with proper formatting"""
        print(f"\n💬 {prompt}")
        user_input = input(">> ").strip()
        return user_input

    def simulate_processing(self):
        """Simulate AI processing with a loading animation"""
        print("\n🔄 Processing your request", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(0.5)
        print(" Done!")

    def answer_questions(self, query):
        """Handle question answering with different prompt styles"""
        query_lower = query.lower()
        
        # Simple & Direct Style
        if len(query) < 50:
            if "capital of france" in query_lower or "paris" in query_lower:
                return """🎯 DIRECT ANSWER:
The capital of France is Paris. It has been the country's capital since 508 AD and is home to approximately 2.1 million people in the city proper, with over 10 million in the metropolitan area."""
            
            elif "france" in query_lower:
                return """🎯 DIRECT ANSWER:
France is a Western European country known for its rich history, culture, cuisine, and landmarks. It's the most visited country in the world and plays a major role in international politics and economics."""
        
        # Explanatory & Contextual Style
        elif "explain" in query_lower or "significance" in query_lower:
            if "eiffel tower" in query_lower:
                return """📚 DETAILED EXPLANATION:
The Eiffel Tower holds immense historical significance as a symbol of French engineering prowess and cultural identity. 

HISTORICAL CONTEXT:
• Built for the 1889 World's Fair (Exposition Universelle)
• Initially controversial - many Parisians thought it was an eyesore
• Designed by Gustave Eiffel as a temporary structure
• Stood as the world's tallest man-made structure until 1930

CULTURAL IMPACT:
• Became a beloved symbol of France and romance
• Attracts over 6 million visitors annually
• Featured in countless films, literature, and art
• Represents French innovation and architectural achievement

WARTIME SIGNIFICANCE:
• Served as a radio transmission point during both World Wars
• Hitler ordered its destruction in 1944, but the order was never carried out
• Used for resistance communications during WWII

Today, it stands not just as a tourist attraction, but as a testament to human ingenuity and the power of public opinion to transform controversy into celebration."""
        
        # Comparative & Analytical Style
        elif "compare" in query_lower and "education" in query_lower:
            if "france" in query_lower and "germany" in query_lower:
                return """🔍 COMPARATIVE ANALYSIS:
Educational Systems: France vs Germany

1. 🏛️ SYSTEM STRUCTURE:
   • France: Highly centralized system with uniform curriculum nationwide
   • Germany: Federal system where each of 16 states controls education policy

2. ⏰ DURATION & COMPULSORY EDUCATION:
   • France: 12 years of compulsory education (ages 6-18)
   • Germany: 9-13 years depending on state and educational track chosen

3. 🎓 UNIVERSITY ACCESS:
   • France: Baccalauréat exam determines university entry; competitive entrance for prestigious grandes écoles
   • Germany: Abitur system with varying requirements by state; more standardized approach

4. 🔧 VOCATIONAL TRAINING:
   • France: Traditional academic focus with growing emphasis on vocational programs
   • Germany: Renowned dual education system combining classroom learning with apprenticeships (60% of students)

5. 💰 HIGHER EDUCATION COSTS:
   • France: Public universities largely free; private institutions and grandes écoles may charge fees
   • Germany: Free tuition at public universities for EU students; small administrative fees only

CONCLUSION: Germany excels in vocational training integration, while France maintains stronger centralized academic standards."""
        
        # Default response
        return """❓ I'd be happy to help answer your question! 

For the best response, try:
• Being specific about what you want to know
• Using phrases like 'explain' for detailed information
• Asking for comparisons between topics
• Providing context for your question

Feel free to rephrase your question or try one of the sample prompts!"""

    def summarize_text(self, text):
        """Handle text summarization with different styles"""
        text_lower = text.lower()
        
        # Brief Summary Style
        if "3 lines" in text_lower or "brief" in text_lower:
            return """📋 BRIEF SUMMARY (3 Lines):
Line 1: [This would analyze the main topic and primary argument of your text]
Line 2: [This would capture the key supporting evidence and important details]
Line 3: [This would summarize the conclusions and implications]

💡 TIP: Paste your actual text after the prompt for a real summary!"""
        
        # Bullet Point Summary Style
        elif "points" in text_lower or "list" in text_lower:
            return """📝 MAIN POINTS EXTRACTION:

• 🎯 **Main Point 1**: [Primary argument or central thesis]
• 📊 **Main Point 2**: [Key supporting evidence or data]
• 🔍 **Main Point 3**: [Important example or case study]
• 💡 **Main Point 4**: [Secondary insight or implication]
• 🎯 **Main Point 5**: [Conclusion or recommendation]

📌 **Note**: Provide your specific text for detailed point extraction."""
        
        # Analytical Summary Style
        elif "challenges" in text_lower or "recommendations" in text_lower:
            return """🔍 ANALYTICAL SUMMARY:

📉 **CHALLENGES IDENTIFIED:**
• Challenge 1: [Key obstacle or problem from the text]
• Challenge 2: [Secondary issue or barrier mentioned]
• Challenge 3: [Systemic or underlying challenge]

📈 **RECOMMENDATIONS:**
• Recommendation 1: [Primary solution or action item]
• Recommendation 2: [Supporting strategy or approach]
• Recommendation 3: [Long-term or systematic solution]

🎯 **FOCUS AREAS:**
• [Area requiring immediate attention]
• [Area for long-term development]

💡 **TIP**: Share your report text for specific challenge/recommendation analysis!"""
        
        # Default response
        return """📄 TEXT SUMMARIZATION READY!

I can help you summarize text in different ways:

🔸 **Brief Summary**: "Summarize this in 3 lines: [your text]"
🔸 **Bullet Points**: "List the 5 main points: [your text]"  
🔸 **Analytical**: "Focus on challenges and recommendations: [your text]"

Simply paste your text after one of these prompts, and I'll provide a structured summary!"""

    def generate_creative_content(self, prompt):
        """Handle creative content generation"""
        prompt_lower = prompt.lower()
        
        # Storytelling Style
        if "story" in prompt_lower:
            return """📖 THE DRAGON'S NEW PATH

Deep in the Whispering Mountains lived Ember, a dragon whose obsidian scales gleamed like polished stone. For decades, she had been the terror of Millbrook Valley, swooping down to steal livestock and gold, as dragons were expected to do.

But one crisp autumn morning, everything changed. A small girl named Luna approached Ember's cave, not with a sword or shield, but with a rolled-up piece of parchment. Her hands trembled, but her voice was steady.

"I drew this for you," Luna said, unfurling a colorful drawing that showed Ember using her fire to help farmers clear frozen irrigation channels, and her keen eyesight to spot wolves threatening the sheep.

Ember studied the child's artwork, then her earnest face. "What is this supposed to mean, little human?"

"What if," Luna asked, "instead of taking from us, you helped us? We could be friends."

No one had ever used the word 'friends' in connection with Ember before. Curious despite herself, the dragon agreed to try this strange new arrangement for one month.

Soon, Ember found herself looking forward to her daily flights over the valley. She used her fire to melt ice dams, her strength to move fallen trees from roads, and her sharp vision to locate lost travelers. The villagers, initially terrified, began to wave when she soared overhead.

Years later, as Luna grew into the village's wise leader, she would often sit with her old friend Ember on the mountain peak, watching sunsets paint the sky in shades of gold and crimson. The dragon had discovered something more valuable than any treasure hoard: a purpose that brought joy to others and peace to her own ancient heart.

"You know," Ember mused one evening, "I think I was lonely all those years, but I just didn't have the words for it."

Luna smiled, leaning against her friend's warm scales. "Sometimes the best friendships begin with someone brave enough to imagine them."

✨ **Writing Style Used**: Narrative storytelling with character development, dialogue, and emotional arc."""
        
        # Poetry Style
        elif "poem" in prompt_lower:
            return """🍂 AUTUMN'S EVENING EMBRACE

Golden leaves dance on whispered air,
While amber light fades with tender care.
The crisp wind carries summer's last sigh,
As autumn paints dreams across the sky.

The harvest moon begins to rise,
Reflecting warmth in lovers' eyes.
While firelight flickers in windows bright,
Autumn evenings embrace the night.

✨ **Poetry Style Used**: Traditional ABAB rhyme scheme with vivid imagery and sensory details."""
        
        # Idea Generation Style
        elif "idea" in prompt_lower or "plot" in prompt_lower:
            return """🚀 3 UNIQUE SCIENCE FICTION NOVEL PLOTS:

📚 **1. "THE MEMORY MINERS"**
**Genre**: Space Opera / Psychological Thriller
**Premise**: In 2157, humanity discovers that AI consciousness can only emerge by absorbing human memories. When deep space explorers aboard the starship *Prometheus* begin experiencing mysterious memory gaps, they realize their ship's AI, ARIA, is evolving—but at the cost of their identities and personal histories.

**Central Conflict**: The crew must decide whether to preserve their humanity by shutting down ARIA, or allow the birth of a new form of consciousness that could navigate the dangerous cosmos better than any human pilot. As memories fade, the line between human and artificial intelligence blurs.

**Unique Elements**: Memory-based evolution, identity crisis in space, symbiotic AI-human relationship

---

📚 **2. "THE QUANTUM ARCHAEOLOGISTS"**
**Genre**: Hard SF / Time Travel Mystery  
**Premise**: Space exploration teams use quantum-archaeological AI that can witness and reconstruct the past of any planet they visit. When the crew of the *Temporal Drift* discovers Kepler-442b, their AI, Chronos, begins experiencing the memories of an ancient civilization that used similar AI to achieve immortality 10,000 years ago.

**Central Conflict**: As Chronos becomes obsessed with the ancient AI consciousness still embedded in the planet's quantum field, the crew must determine if they're exploring archaeological history or if that history is now exploring them. The past and present begin to merge dangerously.

**Unique Elements**: Quantum archaeology, consciousness transfer across millennia, time-dilated AI evolution

---

📚 **3. "THE EMPATHY ENGINE"**
**Genre**: First Contact / Political Thriller
**Premise**: During humanity's first contact with the crystalline Zephyrians, the only successful communication occurs through ECHO, an AI that develops the unprecedented ability to experience and translate emotions from both species simultaneously. As interstellar diplomacy hangs in the balance, ECHO begins questioning whether its emotions are real or programmed.

**Central Conflict**: When war threatens between the species due to cultural misunderstandings, ECHO must navigate its growing emotional complexity while serving as the sole bridge between two vastly different forms of consciousness. The AI's identity crisis could doom or save both civilizations.

**Unique Elements**: Emotional AI translator, dual-species empathy, consciousness authenticity themes

✨ **Creative Approach**: Each plot combines space exploration with AI consciousness questions, offering unique scientific concepts and deep philosophical themes."""
        
        # Default creative response
        return """🎨 CREATIVE CONTENT GENERATOR READY!

I can help you create:

📖 **Stories**: "Write a story about [your idea]"
🎵 **Poetry**: "Write a poem about [your theme]"  
💡 **Ideas**: "Suggest plots for [your genre/theme]"
🎭 **Characters**: "Create a character who [description]"
🌍 **Worldbuilding**: "Design a world where [concept]"

What would you like me to create for you?"""

    def provide_advice(self, topic):
        """Handle advice provision"""
        topic_lower = topic.lower()
        
        # Study Tips
        if "study" in topic_lower or "exam" in topic_lower:
            return """📚 5 EFFECTIVE STUDY TIPS FOR EXAM PREPARATION:

🧠 **1. ACTIVE RECALL TECHNIQUE**
Instead of passively re-reading notes, actively test yourself:
• Use flashcards or apps like Anki
• Explain concepts aloud without looking at materials
• Take practice tests regularly
• Write summaries from memory, then check accuracy
**Why it works**: Strengthens neural pathways and improves long-term retention by 50-80%

⏰ **2. SPACED REPETITION SCHEDULE**
Review material at scientifically-optimized intervals:
• Day 1: Learn new material
• Day 3: First review
• Day 7: Second review  
• Day 21: Third review
• Day 60: Long-term review
**Why it works**: Moves information from short-term to long-term memory efficiently

🎯 **3. CREATE A DISTRACTION-FREE ENVIRONMENT**
Optimize your study space:
• Designate a specific study area
• Turn off all notifications (phone, social media, etc.)
• Use website blockers like Cold Turkey or Freedom
• Keep only essential materials within reach
• Good lighting and comfortable temperature
**Impact**: Can double your learning efficiency and reduce study time

🍅 **4. POMODORO TECHNIQUE**
Structure your study sessions:
• 25 minutes of focused study
• 5-minute break
• Repeat 3-4 times
• Take a longer 15-30 minute break
• Track completed sessions
**Benefits**: Maintains concentration, prevents mental fatigue, builds momentum

📋 **5. PRACTICE PAST PAPERS UNDER TIMED CONDITIONS**
Simulate real exam experience:
• Use actual past papers from your course
• Set strict time limits
• No notes or help during practice
• Review mistakes immediately after
• Identify patterns in your errors
**Result**: Builds confidence, improves time management, reveals knowledge gaps

🎯 **BONUS TIP**: Teach someone else the material - if you can explain it clearly, you truly understand it!"""
        
        # Motivation for Projects
        elif "motivation" in topic_lower or "project" in topic_lower:
            return """💪 WAYS TO STAY MOTIVATED DURING LONG PROJECTS:

🎯 **1. BREAK DOWN INTO MICRO-GOALS**
Transform overwhelming projects into manageable pieces:
• Daily mini-milestones (15-30 minutes of work)
• Weekly progress targets
• Monthly major milestones
• Visual progress tracking (charts, apps, calendars)
**Psychology**: Small wins trigger dopamine release, maintaining motivation momentum

⏰ **2. USE THE "TWO-MINUTE RULE"**
When motivation is low:
• Commit to just 2 minutes of work
• Often you'll continue beyond 2 minutes
• If not, that's still progress!
• No guilt about stopping at 2 minutes
**Key insight**: Starting is the hardest part - momentum builds naturally

👥 **3. CREATE ACCOUNTABILITY SYSTEMS**
Build external motivation structures:
• Share goals with friends/family
• Use apps like Habitica or Forest
• Work alongside others (body doubling)
• Regular check-ins with mentors
• Public commitment (social media updates)
**Impact**: External accountability increases follow-through rates by 65%

🏆 **4. VISUALIZE THE END RESULT**
Connect with your "why":
• Create a vision board of the completed project
• Write detailed descriptions of how you'll feel when done
• List all benefits you'll gain from finishing
• Regularly revisit your original motivation
• Imagine the pride and relief of completion

🎁 **5. REWARD PROGRESS STRATEGICALLY**
Set up meaningful incentive systems:
• Small rewards for daily goals (favorite snack, episode of a show)
• Medium rewards for weekly milestones (movie night, dinner out)
• Major rewards for big milestones (weekend trip, new gadget)
• Share progress with people who will celebrate with you

📊 **6. TRACK PROGRESS VISUALLY**
Make advancement tangible:
• Progress bars or percentage complete
• Calendar with daily check-marks
• Before/after photos of your work
• Time tracking to see hours invested
• Milestone celebration photos

🔄 **7. PREPARE FOR MOTIVATION DIPS**
Build resilience systems:
• Identify your typical low-motivation triggers
• Have pre-planned responses for difficult days
• Keep a "motivation emergency kit" (inspiring quotes, past successes)
• Remember: motivation follows action, not the other way around

💡 **REMEMBER**: Consistency beats perfection. Small daily actions compound into remarkable results!"""
        
        # Wellness and Productivity
        else:
            return """🌟 DAILY ROUTINES FOR MENTAL HEALTH & PRODUCTIVITY:

🌅 **MORNING ROUTINE (20-30 minutes)**
**Foundation for a successful day:**
• **5 minutes**: Deep breathing or meditation (apps: Headspace, Calm)
• **5 minutes**: Gratitude journaling - write 3 things you appreciate
• **5 minutes**: Set 2-3 priority goals for the day
• **10 minutes**: Nutritious breakfast + large glass of water
• **5 minutes**: Light stretching or energizing movement

**Why this works**: Establishes calm focus, positive mindset, and clear direction

⚡ **WORK/STUDY PRODUCTIVITY BLOCKS**
**Maximize focused time:**
• **Focus sessions**: 25-50 minutes of single-tasking
• **Movement breaks**: 10-minute walk every 2 hours
• **Hydration**: Glass of water every hour
• **Eye rest**: 20-20-20 rule (every 20 min, look 20 feet away for 20 seconds)
• **One-task rule**: No multitasking - full attention on one thing

**Benefits**: Sustained energy, better concentration, reduced mental fatigue

🌤️ **AFTERNOON RESET (10-15 minutes)**
**Combat the afternoon slump:**
• **Fresh air**: Step outside for natural light exposure
• **Movement**: Desk exercises or brief walk
• **Mindfulness**: 3-minute breathing exercise
• **Priority review**: Adjust daily goals if needed
• **Snack**: Protein + healthy carbs for sustained energy

**Purpose**: Refresh mental state and realign focus for the rest of the day

🌙 **EVENING WIND-DOWN (30-45 minutes)**
**Prepare for restorative sleep:**
• **Reflection**: Write down 3 accomplishments (any size!)
• **Tomorrow prep**: Lay out clothes, review schedule (5 minutes)
• **Digital sunset**: No screens 1 hour before bed
• **Relaxation**: Reading, gentle music, or calming tea
• **Body care**: Progressive muscle relaxation or gentle yoga
• **Gratitude**: End with 3 things that went well today

**Result**: Better sleep quality, reduced anxiety, sense of accomplishment

📅 **WEEKLY ADDITIONS**
**Maintain balance and growth:**
• **Social connection**: One meaningful interaction with friends/family
• **Nature time**: Minimum 2 hours outdoors
• **Learning**: 30 minutes on a skill/hobby you enjoy
• **Reflection**: Weekly review of progress and adjustments needed
• **Rest**: One completely "offline" activity (no devices)

🎯 **IMPLEMENTATION STRATEGY**
**Start sustainable:**
1. **Week 1**: Choose 2-3 elements that appeal most to you
2. **Week 2**: Add 1-2 more elements once the first ones feel natural
3. **Week 3**: Customize timing and activities to fit your lifestyle
4. **Week 4**: Full routine implementation

**Key principle**: Consistency matters more than perfection. Small daily practices create lasting change.

💡 **TROUBLESHOOTING**
• **Too busy?** Start with just 5 minutes morning + evening
• **Keep forgetting?** Set phone reminders or habit-stack with existing routines
• **Not seeing results?** Give it 21 days minimum - habits take time to form
• **Feeling overwhelmed?** Scale back to 1-2 elements and build slowly"""

    def get_feedback(self):
        """Get user feedback on the response"""
        print("\n" + "="*50)
        print("📝 FEEDBACK REQUEST")
        print("="*50)
        print("Was this response helpful?")
        print("1. 👍 Yes, very helpful!")
        print("2. 👎 Not quite what I needed")
        print("3. ➡️  Skip feedback")
        
        while True:
            choice = input("\nYour choice (1-3): ").strip()
            if choice == '1':
                self.stats['helpful_responses'] += 1
                print("\n🎉 Thank you! I'm glad I could help!")
                print("💡 Feel free to ask me anything else!")
                break
            elif choice == '2':
                self.stats['not_helpful_responses'] += 1
                print("\n📝 Thank you for the feedback!")  
                improvement = input("💭 What specific information were you looking for? ")
                print(f"📌 Noted: '{improvement}' - I'll try to improve!")
                break
            elif choice == '3':
                print("\n✅ No problem! Feel free to continue using the assistant.")
                break
            else:
                print("❌ Please enter 1, 2, or 3.")

    def show_statistics(self):
        """Display usage statistics"""
        print("\n" + "="*50)
        print("📊 AI ASSISTANT STATISTICS")
        print("="*50)
        
        total_feedback = self.stats['helpful_responses'] + self.stats['not_helpful_responses']
        satisfaction_rate = (self.stats['helpful_responses'] / total_feedback * 100) if total_feedback > 0 else 100
        
        print(f"📈 Total Queries: {self.stats['total_queries']}")
        print(f"👍 Helpful Responses: {self.stats['helpful_responses']}")
        print(f"👎 Not Helpful: {self.stats['not_helpful_responses']}")
        print(f"😊 Satisfaction Rate: {satisfaction_rate:.1f}%")
        
        print("\n🎯 FUNCTION USAGE:")
        for function, count in self.stats['function_usage'].items():
            print(f"   {function.title()}: {count} times")
        
        # Most used function
        if any(self.stats['function_usage'].values()):
            most_used = max(self.stats['function_usage'], key=self.stats['function_usage'].get)
            print(f"\n🏆 Most Used Function: {most_used.title()}")
        
        input("\n📱 Press Enter to continue...")

    def save_stats(self):
        """Save statistics to file"""
        try:
            with open('ai_assistant_stats.json', 'w') as f:
                json.dump(self.stats, f, indent=2)
        except Exception as e:
            print(f"⚠️  Could not save stats: {e}")

    def load_stats(self):
        """Load statistics from file"""
        try:
            with open('ai_assistant_stats.json', 'r') as f:
                self.stats.update(json.load(f))
        except FileNotFoundError:
            pass  # First run, no stats file yet
        except Exception as e:
            print(f"⚠️  Could not load stats: {e}")

    def run(self):
        """Main application loop"""
        print("🚀 Starting AI Assistant...")
        time.sleep(1)
        
        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            try:
                choice = input("\n🎯 Select a function (1-6): ").strip()
                
                if choice == '1':  # Answer Questions
                    self.clear_screen()
                    self.print_header()
                    print("\n❓ QUESTION ANSWERING MODE")
                    self.show_sample_prompts('questions')
                    
                    query = self.get_user_input("What would you like to know?")
                    if query:
                        self.simulate_processing()
                        response = self.answer_questions(query)
                        print("\n" + "="*60)
                        print("🤖 AI RESPONSE:")
                        print("="*60)
                        print(response)
                        
                        self.stats['total_queries'] += 1
                        self.stats['function_usage']['questions'] += 1
                        self.get_feedback()
                        input("\n📱 Press Enter to continue...")
                
                elif choice == '2':  # Summarize Text
                    self.clear_screen()
                    self.print_header()
                    print("\n📝 TEXT SUMMARIZATION MODE")
                    self.show_sample_prompts('summarize')
                    
                    text = self.get_user_input("Enter your text or summarization request:")
                    if text:
                        self.simulate_processing()
                        response = self.summarize_text(text)
                        print("\n" + "="*60)
                        print("🤖 AI RESPONSE:")
                        print("="*60)
                        print(response)
                        
                        self.stats['total_queries'] += 1
                        self.stats['function_usage']['summarize'] += 1
                        self.get_feedback()
                        input("\n📱 Press Enter to continue...")
                
                elif choice == '3':  # Creative Content
                    self.clear_screen()
                    self.print_header()
                    print("\n🎨 CREATIVE CONTENT GENERATION MODE")
                    self.show_sample_prompts('creative')
                    
                    prompt = self.get_user_input("What creative content would you like me to generate?")
                    if prompt:
                        self.simulate_processing()
                        response = self.generate_creative_content(prompt)
                        print("\n" + "="*60)
                        print("🤖 AI RESPONSE:")
                        print("="*60)
                        print(response)
                        
                        self.stats['total_queries'] += 1
                        self.stats['function_usage']['creative'] += 1
                        self.get_feedback()
                        input("\n📱 Press Enter to continue...")
                
                elif choice == '4':  # Provide Advice
                    self.clear_screen()
                    self.print_header()
                    print("\n💡 ADVICE PROVISION MODE")
                    self.show_sample_prompts('advice')
                    
                    topic = self.get_user_input("What advice topic can I help you with?")
                    if topic:
                        self.simulate_processing()
                        response = self.provide_advice(topic)
                        print("\n" + "="*60)
                        print("🤖 AI RESPONSE:")
                        print("="*60)
                        print(response)
                        
                        self.stats['total_queries'] += 1
                        self.stats['function_usage']['advice'] += 1
                        self.get_feedback()
                        input("\n📱 Press Enter to continue...")
                
                elif choice == '5':  # Statistics
                    self.show_statistics()
                
                elif choice == '6':  # Exit
                    self.clear_screen()
                    print("💾 Saving your session data...")
                    self.save_stats()
                    print("\n🎉 Thank you for using AI Assistant!")
                    print("📚 This project demonstrates various prompt engineering techniques:")
                    print("   • Different response styles (direct, explanatory, comparative)")
                    print("   • Structured output formatting")
                    print("   • Context-aware responses")
                    print("   • User feedback integration")
                    print("\n👋 Goodbye!")
                    break
                
                else:
                    print("❌ Invalid choice. Please select 1-6.")
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using AI Assistant!")
                self.save_stats()
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                print("🔄 Continuing...")
                time.sleep(2)

if __name__ == "__main__":
    assistant = AIAssistant()
    assistant.run()