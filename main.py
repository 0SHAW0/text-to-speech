from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from TTS.api import TTS
import torch
import io
import soundfile as sf

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC").to(device)

class TextInput(BaseModel):
    text: str

@app.post("/speak")
async def speak(request: TextInput):
    try:
        text = request.text.strip().replace("’", "'").replace("—", "-")
        if not text:
            return {"error": "Empty input."}

        print("Generating audio for:", text)
        wav = tts.tts(text)

        buffer = io.BytesIO()
        sf.write(buffer, wav, 22050, format='WAV')
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="audio/wav")

    except Exception as e:
        print(" ERROR:", str(e))
        return {"error": str(e)}
