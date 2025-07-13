#!/bin/bash

echo "🤖 Setting up ShadBot..."
echo "📦 Installing Python packages..."

# Install required packages
pip install flask nltk

echo "📚 Downloading NLTK data..."
python -c "
import nltk
print('Downloading punkt...')
nltk.download('punkt')
print('Downloading stopwords...')
nltk.download('stopwords') 
print('Downloading wordnet...')
nltk.download('wordnet')
print('✅ NLTK data downloaded successfully!')
"

echo "🚀 Setup complete! Starting ShadBot..."
python main.py
