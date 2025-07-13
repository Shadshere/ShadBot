#!/bin/bash

echo "🤖 Starting ShadBot on Replit..."
echo "📦 Installing dependencies..."

# Install Python dependencies
pip install -r requirements.txt

echo "🚀 Starting ShadBot Web Server..."
echo "🌐 Your chatbot will be available at the Replit URL"

# Run the main application
python main.py
