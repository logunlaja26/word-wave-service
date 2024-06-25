from fastapi import APIRouter, Depends, HTTPException, Query
from transcribeFunction import transcribe_audio
from transcribeProcessor import transcribe_audio_replicate
from pydantic import BaseModel
from fileLocationFinder import file_location


router = APIRouter()

class TranscribeRequest(BaseModel):
    url: str


@router.post("/transcribe")
async def transcibeAudio(request: TranscribeRequest):
    try:
        transcript = transcribe_audio_replicate(request.url)
        return transcript
    except Exception as e:
        print("Error...", e)
        raise HTTPException(status_code=500, detail="An error occurred during transcription.")  