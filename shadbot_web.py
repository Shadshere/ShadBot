from flask import Flask, render_template, request, jsonify
import json
import re
import random
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

class ShadBotWeb:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.user_sessions = {}  # Store user data per session
        self.load_responses()
    
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
                    "You can contact Amirul at 019-9095792 or <a href='https://wa.me/+60199095792?text=Hello%20Amirul%20' target='_blank' class='whatsapp-link'>click here to WhatsApp</a>",
                    "For direct contact, call 019-9095792 or <a href='https://wa.me/+60199095792?text=Hello%20Amirul%20' target='_blank' class='whatsapp-link'>WhatsApp Amirul</a>"
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
    
    def preprocess_text(self, text):
        """Preprocess text using NLTK"""
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words and token.isalpha()]
        return tokens
    
    def detect_intent(self, user_input):
        """Detect user intent based on keywords"""
        text_lower = user_input.lower()
        
        if re.search(r'my name is (\w+)', text_lower):
            return 'name'
        
        greeting_words = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'greetings']
        if any(word in text_lower for word in greeting_words):
            return 'greeting'
        
        farewell_words = ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit']
        if any(word in text_lower for word in farewell_words):
            return 'farewell'
        
        gratitude_words = ['thank', 'thanks', 'appreciate', 'grateful']
        if any(word in text_lower for word in gratitude_words):
            return 'gratitude'
        
        hours_words = ['hours', 'time', 'open', 'close', 'working', 'office']
        if any(word in text_lower for word in hours_words):
            return 'hours'
        
        services_words = ['service', 'help', 'do', 'offer', 'provide', 'assist']
        if any(word in text_lower for word in services_words) and 'what' in text_lower:
            return 'services'
        
        contact_words = ['contact', 'phone', 'number', 'call', 'reach', 'whatsapp']
        if any(word in text_lower for word in contact_words):
            return 'contact'
        
        joke_words = ['joke', 'funny', 'humor', 'laugh', 'entertainment']
        if any(word in text_lower for word in joke_words):
            return 'joke'
        
        if re.search(r'[\d+\-*/()]+', user_input) or any(word in text_lower for word in ['calculate', 'math', 'plus', 'minus', 'multiply', 'divide']):
            return 'math'
        
        return 'unknown'
    
    def handle_math(self, user_input):
        """Handle simple math calculations"""
        try:
            match = re.search(r'[\d+\-*/().\s]+', user_input)
            if match:
                expression = match.group().strip()
                if re.match(r'^[\d+\-*/().\s]+$', expression):
                    result = eval(expression)
                    return f"The answer is: {result}"
            return "I can help with basic math! Try something like '5 + 3' or '10 * 2'"
        except:
            return "Sorry, I couldn't calculate that. Please try a simpler math expression."
    
    def get_response(self, user_input, session_id):
        """Get appropriate response based on user input"""
        if session_id not in self.user_sessions:
            self.user_sessions[session_id] = {'name': None}
        
        intent = self.detect_intent(user_input)
        
        if intent == 'name':
            match = re.search(r'my name is (\w+)', user_input.lower())
            if match:
                self.user_sessions[session_id]['name'] = match.group(1).capitalize()
                return f"Nice to meet you, {self.user_sessions[session_id]['name']}! How can I help you today?"
        
        elif intent == 'greeting':
            response = random.choice(self.responses['greetings'])
            if self.user_sessions[session_id]['name']:
                response = f"Hello again, {self.user_sessions[session_id]['name']}! " + response
            return response
        
        elif intent == 'farewell':
            response = random.choice(self.responses['farewell'])
            if self.user_sessions[session_id]['name']:
                response = f"Goodbye, {self.user_sessions[session_id]['name']}! " + response
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

# Flask App
app = Flask(__name__)
chatbot = ShadBotWeb()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    if user_message:
        bot_response = chatbot.get_response(user_message, session_id)
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
    
    return jsonify({
        'response': 'Please enter a message!',
        'status': 'error'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
