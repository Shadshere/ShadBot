#!/usr/bin/env python3
"""
ShadBot - AI Chatbot for Replit
Main entry point for the web-based version
"""

import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import and run the web version
from shadbot_web import app

if __name__ == '__main__':
    # Get port from environment variable (Replit sets this automatically)
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask app
    # host='0.0.0.0' makes it accessible from outside
    # debug=False for production
    app.run(host='0.0.0.0', port=port, debug=False)
