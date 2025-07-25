#!/bin/bash

echo "🔧 Creating virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# echo "🛡️ Creating .env file..."
# cat <<EOF > .env
# # Add your OpenAI API key below
# OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# EOF

echo "✅ All set! To run your app:"
echo "1. Activate the environment: source venv/bin/activate"
echo "2. Start the app: uvicorn main:app --reload"
