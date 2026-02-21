# 🩺 AI Doctor with Vision and Voice

## 🚀 Overview
AI Doctor is a Multimodal Healthcare Assistant that analyzes patient voice symptoms and medical images to provide preliminary medical guidance using AI.

## 🎯 Problem Statement
Many rural and remote areas lack immediate access to healthcare professionals. This project provides an AI-powered preliminary diagnostic assistant using voice and image analysis.

## 🧠 Key Features
- 🎤 Voice Symptom Input (Speech-to-Text using Whisper via Groq)
- 🖼️ Medical Image Analysis (Vision LLM)
- 🔊 AI Doctor Voice Response (ElevenLabs TTS)
- 🌐 Interactive Gradio Web Interface
- ⚡ Real-time Multimodal AI Diagnosis

## 🏗️ System Architecture
Patient Voice → Speech-to-Text → Image + Symptoms → Multimodal LLM → Doctor Response → Voice Output

## 🛠️ Tech Stack
- Python
- Gradio
- Groq API (Whisper + LLM)
- ElevenLabs API (Text-to-Speech)
- Multimodal AI (Vision + Voice)

## ▶️ How to Run the Project
```bash
git clone https://github.com/Harshdaadale/AI-Doctor-with-vision-and-voice.git
cd AI-Doctor-with-vision-and-voice
pip install -r requirements.txt
python gradio_app.py
