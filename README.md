#  Text-to-Speech (TTS) Web App using FastAPI and Coqui TTS

This is a lightweight text-to-speech (TTS) application built using **FastAPI** and **Coqui TTS**. It allows users to input English text, convert it to speech, and listen to the output directly in the browser. The model can also be accessed via a POST API (like OpenAI-style SDKs).

---

##  Features

- ✅ FastAPI-based backend
- ✅ Converts English text to speech
- ✅ Clean browser UI (dark theme)
- ✅ Returns audio in real time
- ✅ Compatible with OpenAI SDK-style API calls
- ❌ Accent training (incomplete — see below)

---

##  Indian Accent Support Disclosure

I have included a folder `my_voice_dataset/` which contains:
- A folder `wavs/` with 9 audio samples of **my own voice**
- A `metadata.csv` file describing these samples
- A file `your_voice.wav` used for basic cloning attempts

> While I tried to fine-tune the XTTS model using this dataset to generate an Indian-accented English voice, I was **not successful** in training it fully due to environment constraints.  
> This is documented and preserved in the repo for future fine-tuning.

---

##  Local Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/text-to-speech-app.git
cd text-to-speech-app
2. Create virtual environment & activate

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt

4. Run the FastAPI server

uvicorn main:app --reload

5. Open the frontend

Double-click frontend.html to open in your browser or open it with live server.

Enter some text and click Convert.

 Example OpenAI-style API Call (Python)
import requests

response = requests.post("http://127.0.0.1:8000/speak", json={
    "text": "This is a test using OpenAI-style call."
})

if response.status_code == 200:
    with open("output.wav", "wb") as f:
        f.write(response.content)
    print(" Saved to output.wav")
else:
    print(" Request failed:", response.status_code)
 Optional Cloud Deployment (Not done)


This project is built in a way that can be deployed on:

Render

Hugging Face Spaces (with Gradio frontend)

Railway / Fly.io / Replit

Due to time and resource limits, this project remains local-only for now. However, it can easily be containerized or deployed via uvicorn + ngrok.

 Project Structure
css
Copy
Edit
text-to-speech-app/
├── main.py
├── frontend.html
├── README.md
├── requirements.txt
├── your_voice.wav
└── my_voice_dataset/
    ├── metadata.csv
    └── wavs/
        ├── voice1.wav
        ├── voice2.wav
        └── ...
Requirements
Dependencies (in requirements.txt):

fastapi
uvicorn
pydantic
torch>=2.0.0
TTS>=0.22.0
soundfile
Install them via:

pip install -r requirements.txt

Final Submission Checklist
Complete codebase	 Done
README with all required sections	 Done
Working local FastAPI TTS app	 Done
Hindi/Indian accent support	 Not working (dataset included)
Hosted demo	 Not hosted (future work)

 Submission
This project is completed to the best of my effort and prepared as a final deliverable.


 Author Note
This project was completed with a model supporting english voice only.
Fine-tuning was attempted but left incomplete and may be revisited in future versions.