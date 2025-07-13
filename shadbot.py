import tkinter as tk
from tkinter import scrolledtext, messagebox
import json
import re
import random
import webbrowser
from datetime import datetime
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

class ShadBot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.user_name = None
        self.load_responses()
        self.setup_gui()
        
    def load_responses(self):
        """Load chatbot responses from JSON file"""
        try:
            with open('responses.json', 'r', encoding='utf-8') as file:
                self.responses = json.load(file)
        except FileNotFoundError:
            # Create default responses if file doesn't exist
            self.responses = {
                "greetings": [
                    "Hi there! How can I help you?",
                    "Hello! Nice to meet you!",
                    "Hey! What can I do for you today?",
                    "Greetings! How are you doing?"
                ],
                "farewell": [
                    "Goodbye! Have a great day!",
                    "See you later! Take care!",
                    "Bye! It was nice talking to you!",
                    "Farewell! Come back anytime!"
                ],
                "gratitude": [
                    "You're welcome! 😊",
                    "Happy to help! 🙂",
                    "No problem at all!",
                    "Glad I could assist you!"
                ],
                "hours": [
                    "We're open 9 AM to 5 PM, Monday to Friday.",
                    "Our working hours are 9:00 AM to 5:00 PM on weekdays.",
                    "Office hours: Monday-Friday, 9 AM - 5 PM."
                ],
                "services": [
                    "I can help you with basic questions, provide information about our services, tell jokes, and do simple math!",
                    "I offer assistance with FAQs, general information, entertainment, and basic calculations.",
                    "My services include answering questions, providing company info, jokes, and math help."
                ],
                "contact": [
                    "You can contact Amirul at 019-9095792 or click here to WhatsApp: https://wa.me/+60199095792?text=Hello%20Amirul%20",
                    "For direct contact, call 019-9095792 or WhatsApp Amirul: https://wa.me/+60199095792?text=Hello%20Amirul%20"
                ],
                "jokes": [
                    "Why did the computer go to therapy? Because it had too many bugs! 🐞",
                    "Why don't programmers like nature? It has too many bugs! 🌿🐛",
                    "What do you call a computer that sings? A Dell! 🎵",
                    "Why did the developer go broke? Because he used up all his cache! 💰",
                    "How do you comfort a JavaScript bug? You console it! 😄"
                ],
                "unknown": [
                    "I'm still learning! Can you ask me something else?",
                    "I'm not sure about that. Could you try asking something different?",
                    "That's interesting, but I don't have an answer for that yet.",
                    "I'm still growing my knowledge! Ask me about our services, hours, or maybe a joke?"
                ]
            }
            self.save_responses()
    
    def save_responses(self):
        """Save responses to JSON file"""
        with open('responses.json', 'w', encoding='utf-8') as file:
            json.dump(self.responses, file, indent=2, ensure_ascii=False)
    
    def preprocess_text(self, text):
        """Preprocess text using NLTK"""
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words and token.isalpha()]
        
        return tokens
    
    def detect_intent(self, user_input):
        """Detect user intent based on keywords"""
        tokens = self.preprocess_text(user_input)
        text_lower = user_input.lower()
        
        # Check for name input
        if re.search(r'my name is (\w+)', text_lower):
            return 'name'
        
        # Check for greetings
        greeting_words = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings']
        if any(word in text_lower for word in greeting_words):
            return 'greeting'
        
        # Check for farewell
        farewell_words = ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit']
        if any(word in text_lower for word in farewell_words):
            return 'farewell'
        
        # Check for gratitude
        gratitude_words = ['thank', 'thanks', 'appreciate', 'grateful']
        if any(word in text_lower for word in gratitude_words):
            return 'gratitude'
        
        # Check for hours inquiry
        hours_words = ['hours', 'time', 'open', 'close', 'working', 'office']
        if any(word in text_lower for word in hours_words):
            return 'hours'
        
        # Check for services inquiry
        services_words = ['service', 'help', 'do', 'offer', 'provide', 'assist']
        if any(word in text_lower for word in services_words) and 'what' in text_lower:
            return 'services'
        
        # Check for contact inquiry
        contact_words = ['contact', 'phone', 'number', 'call', 'reach', 'whatsapp']
        if any(word in text_lower for word in contact_words):
            return 'contact'
        
        # Check for joke request
        joke_words = ['joke', 'funny', 'humor', 'laugh', 'entertainment']
        if any(word in text_lower for word in joke_words):
            return 'joke'
        
        # Check for math
        if re.search(r'[\d+\-*/()]+', user_input) or any(word in text_lower for word in ['calculate', 'math', 'plus', 'minus', 'multiply', 'divide']):
            return 'math'
        
        return 'unknown'
    
    def handle_math(self, user_input):
        """Handle simple math calculations"""
        try:
            # Extract math expression
            match = re.search(r'[\d+\-*/().\s]+', user_input)
            if match:
                expression = match.group().strip()
                # Basic security check - only allow numbers and basic operators
                if re.match(r'^[\d+\-*/().\s]+$', expression):
                    result = eval(expression)
                    return f"The answer is: {result}"
            
            return "I can help with basic math! Try something like '5 + 3' or '10 * 2'"
        except:
            return "Sorry, I couldn't calculate that. Please try a simpler math expression."
    
    def get_response(self, user_input):
        """Get appropriate response based on user input"""
        intent = self.detect_intent(user_input)
        
        if intent == 'name':
            match = re.search(r'my name is (\w+)', user_input.lower())
            if match:
                self.user_name = match.group(1).capitalize()
                return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        elif intent == 'greeting':
            response = random.choice(self.responses['greetings'])
            if self.user_name:
                response = f"Hello again, {self.user_name}! " + response
            return response
        
        elif intent == 'farewell':
            response = random.choice(self.responses['farewell'])
            if self.user_name:
                response = f"Goodbye, {self.user_name}! " + response
            return response
        
        elif intent == 'gratitude':
            return random.choice(self.responses['gratitude'])
        
        elif intent == 'hours':
            return random.choice(self.responses['hours'])
        
        elif intent == 'services':
            return random.choice(self.responses['services'])
        
        elif intent == 'contact':
            return random.choice(self.responses['contact'])
        
        elif intent == 'joke':
            return random.choice(self.responses['jokes'])
        
        elif intent == 'math':
            return self.handle_math(user_input)
        
        else:
            return random.choice(self.responses['unknown'])
    
    def setup_gui(self):
        """Setup the GUI using Tkinter"""
        self.root = tk.Tk()
        self.root.title("ShadBot - AI Chatbot")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')
        
        # Header
        header_frame = tk.Frame(self.root, bg='#34495e', height=80)
        header_frame.pack(fill='x', padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🤖 ShadBot", 
                              font=('Arial', 24, 'bold'), 
                              bg='#34495e', fg='#ecf0f1')
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(header_frame, text="Your AI Assistant", 
                                 font=('Arial', 12), 
                                 bg='#34495e', fg='#bdc3c7')
        subtitle_label.pack()
        
        # Chat display area
        chat_frame = tk.Frame(self.root, bg='#2c3e50')
        chat_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, 
                                                     wrap=tk.WORD, 
                                                     width=70, 
                                                     height=20,
                                                     font=('Arial', 11),
                                                     bg='#ecf0f1',
                                                     fg='#2c3e50',
                                                     insertbackground='#2c3e50')
        self.chat_display.pack(fill='both', expand=True)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#2c3e50')
        input_frame.pack(fill='x', padx=10, pady=10)
        
        self.user_input = tk.Entry(input_frame, 
                                  font=('Arial', 12), 
                                  bg='#ecf0f1', 
                                  fg='#2c3e50',
                                  insertbackground='#2c3e50')
        self.user_input.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        send_button = tk.Button(input_frame, 
                               text="Send", 
                               command=self.send_message,
                               font=('Arial', 12, 'bold'),
                               bg='#3498db',
                               fg='white',
                               activebackground='#2980b9',
                               activeforeground='white',
                               cursor='hand2')
        send_button.pack(side='right')
        
        # Bind Enter key to send message
        self.user_input.bind('<Return>', lambda event: self.send_message())
        
        # Welcome message
        welcome_message = "🤖 ShadBot: Hello! I'm ShadBot, your AI assistant. I can help you with:\n"
        welcome_message += "• Basic conversations and greetings\n"
        welcome_message += "• Information about our services and hours\n"
        welcome_message += "• Contact information\n"
        welcome_message += "• Jokes and entertainment\n"
        welcome_message += "• Simple math calculations\n"
        welcome_message += "• And much more!\n\n"
        welcome_message += "Try saying 'Hello' or ask me 'What are your hours?' to get started!\n"
        welcome_message += "-" * 60 + "\n\n"
        
        self.chat_display.insert(tk.END, welcome_message)
        self.chat_display.see(tk.END)
        
        # Focus on input field
        self.user_input.focus()
    
    def send_message(self):
        """Handle sending messages"""
        user_message = self.user_input.get().strip()
        if user_message:
            # Display user message
            timestamp = datetime.now().strftime("%H:%M")
            self.chat_display.insert(tk.END, f"[{timestamp}] You: {user_message}\n")
            
            # Get bot response
            bot_response = self.get_response(user_message)
            
            # Handle WhatsApp links
            if "wa.me" in bot_response:
                parts = bot_response.split("https://wa.me/")
                if len(parts) > 1:
                    self.chat_display.insert(tk.END, f"[{timestamp}] 🤖 ShadBot: {parts[0]}")
                    
                    # Create clickable link
                    link_start = self.chat_display.index(tk.INSERT)
                    link_text = "WhatsApp Link"
                    self.chat_display.insert(tk.END, link_text)
                    link_end = self.chat_display.index(tk.INSERT)
                    
                    # Configure link appearance
                    self.chat_display.tag_add("link", link_start, link_end)
                    self.chat_display.tag_config("link", foreground="blue", underline=True)
                    
                    # Bind click event
                    whatsapp_url = "https://wa.me/" + parts[1]
                    self.chat_display.tag_bind("link", "<Button-1>", 
                                             lambda e: webbrowser.open(whatsapp_url))
                    self.chat_display.tag_bind("link", "<Enter>", 
                                             lambda e: self.chat_display.config(cursor="hand2"))
                    self.chat_display.tag_bind("link", "<Leave>", 
                                             lambda e: self.chat_display.config(cursor=""))
                    
                    self.chat_display.insert(tk.END, "\n\n")
                else:
                    self.chat_display.insert(tk.END, f"[{timestamp}] 🤖 ShadBot: {bot_response}\n\n")
            else:
                self.chat_display.insert(tk.END, f"[{timestamp}] 🤖 ShadBot: {bot_response}\n\n")
            
            # Clear input and scroll to bottom
            self.user_input.delete(0, tk.END)
            self.chat_display.see(tk.END)
    
    def run(self):
        """Start the chatbot"""
        self.root.mainloop()

if __name__ == "__main__":
    bot = ShadBot()
    bot.run()
