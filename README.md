# ShadBot 🤖
An intelligent AI-powered chatbot built with Python, featuring Natural Language Processing and a beautiful GUI interface.

## 🌟 Features

![WhatsApp Image 2025-07-13 at 15 56 42_80c13113](https://github.com/user-attachments/assets/778ce260-6a1d-482c-a1ed-ae8d44982c4e)

### Core Capabilities
- **Smart Greetings & Responses** - Friendly and approachable interactions
- **FAQ System** - Information about services, hours, and contact details
- **Gratitude Handling** - Polite responses to thank you messages
- **Simple Memory** - Remembers user's name throughout the conversation
- **Math Helper** - Performs basic mathematical calculations
- **Joke Teller** - Entertainment with programming and tech jokes
- **Fallback Responses** - Handles unknown queries gracefully

### Technical Features
- **Natural Language Processing** using NLTK
- **Beautiful GUI** built with Tkinter
- **JSON-based Response System** for easy customization
- **WhatsApp Integration** - Direct links to contact via WhatsApp
- **Responsive Design** with modern UI elements
- **Real-time Chat Interface** with timestamps

## 🛠️ Technologies Used

- **Python 3.13+** - Core programming language
- **NLTK** - Natural Language Processing and text analysis
- **Tkinter** - GUI framework for desktop application
- **JSON** - Data storage for responses and configurations
- **Regular Expressions** - Pattern matching for intent detection

## 📋 Prerequisites

- Python 3.7 or higher
- Internet connection (for initial NLTK data download)

## 🚀 Try ShadBot Now!

### 🌐 **Instant Online Demo**
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Shadshere/ShadBot)
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Shadshere/ShadBot)

### 📱 **Live Demo Page**
🎯 **Visit**: [https://shadshere.github.io/ShadBot/](https://shadshere.github.io/ShadBot/) *(Enable GitHub Pages to activate)*

## 🚀 Installation & Setup

### Method 1: Quick Start (Recommended)
1. Clone or download this repository
2. Navigate to the project directory
3. Double-click `run_shadbot.bat` to automatically install dependencies and start the chatbot

### Method 2: Manual Installation
1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the chatbot:
   ```bash
   python shadbot.py
   ```

## 💬 How to Use

1. **Start the Application**: Run `shadbot.py` or use the batch file
2. **Begin Chatting**: Type your message in the input field and press Enter or click Send
3. **Try Different Features**:
   - Say "Hello" for greetings
   - Ask "What are your hours?" for business information
   - Say "My name is [Your Name]" to introduce yourself
   - Ask "Tell me a joke" for entertainment
   - Try math like "5 + 3" or "10 * 2"
   - Ask "How can I contact you?" for contact information

## 📞 Contact Integration

The chatbot includes direct WhatsApp integration! When users ask for contact information, they'll get:
- **Phone Number**: 019-9095792
- **WhatsApp Link**: Direct link to chat with Amirul
- **Clickable Links**: Users can click to open WhatsApp directly

## 🎨 User Interface

- **Modern Design**: Clean and professional appearance
- **Dark Theme**: Easy on the eyes with blue accent colors
- **Scrollable Chat**: Full conversation history
- **Timestamps**: Track message timing
- **Clickable Links**: Interactive WhatsApp integration
- **Responsive Layout**: Adapts to different screen sizes

## 📁 Project Structure

```
ShadBot/
├── shadbot.py          # Main chatbot application
├── responses.json      # Chatbot responses database
├── requirements.txt    # Python dependencies
├── run_shadbot.bat     # Quick launcher script
└── README.md          # Project documentation
```

## 🔧 Customization

### Adding New Responses
Edit `responses.json` to add new categories or responses:
```json
{
  "new_category": [
    "Response 1",
    "Response 2"
  ]
}
```

### Modifying Intent Detection
Update the `detect_intent()` method in `shadbot.py` to add new keywords or patterns.

### Changing Contact Information
Update the contact responses in `responses.json` with your own information.

## 🤖 Example Conversations

**Greeting:**
```
User: Hello
ShadBot: Hi there! How can I help you?
```

**Name Memory:**
```
User: My name is Amirul
ShadBot: Nice to meet you, Amirul! How can I help you today?
```

**Math Helper:**
```
User: What's 15 + 25?
ShadBot: The answer is: 40
```

**Jokes:**
```
User: Tell me a joke
ShadBot: Why did the computer go to therapy? Because it had too many bugs! 🐞
```

**Contact Info:**
```
User: How can I contact you?
ShadBot: You can contact Amirul at 019-9095792 or click here to WhatsApp: [WhatsApp Link]
```

## 🚀 Future Enhancements

- [ ] Voice recognition and text-to-speech
- [ ] Machine learning for improved responses
- [ ] Multi-language support
- [ ] Integration with external APIs
- [ ] Advanced conversation memory
- [ ] Sentiment analysis
- [ ] Custom themes and UI options

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Developer

**Amirul**
- Phone: 019-9095792
- WhatsApp: [Click to Chat](https://wa.me/+60199095792?text=Hello%20Amirul%20)

---

Made with ❤️ using Python and NLTK
