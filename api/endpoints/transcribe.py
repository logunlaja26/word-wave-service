from api.datastore.firestore import audio_url
from fastapi import APIRouter, Depends, HTTPException, Query
from transcribeFunction import transcribe_audio
from fileLocationFinder import file_location


router = APIRouter()


# @router.post("/transcribe")
# async def transcibeAudio(file_path: str = Depends(file_location)):
#     try:
#         transcript = transcribe_audio(file_path)
#         return {"transcript": transcript.text}
#     except Exception as e:
#         print("Error...", e)
#         raise HTTPException(status_code=500, detail="An error occurred during transcription.")
    
@router.post("/transcribe")
async def transcibeAudio(file_path: str = Depends(audio_url)):
    try:
        transcript = transcribe_audio(file_path)
        return {"transcript": transcript.text}
    except Exception as e:
        print("Error...", e)
        raise HTTPException(status_code=500, detail="An error occurred during transcription.")    