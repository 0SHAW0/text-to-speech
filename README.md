#  Responsive Text-to-Speech (TTS) App

## Overview

This is a lightweight Text-to-Speech (TTS) web app built with **FastAPI** and **Coqui TTS**.  
It takes text as input and returns speech in real-time using a streaming audio response.  
A simple HTML interface is included to test the app locally.

---

##  Setup Instructions

```bash
git clone https://github.com/your-username/text-to-speech-app.git
cd text-to-speech-app
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
uvicorn main:app --reload