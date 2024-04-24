from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from transcribe import transcribe_audio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/transcribe")
def read_root(audio_url: str):
    try:
        transcript = transcribe_audio(audio_url)
        # if not transcript.status == 'completed':
        #     raise HTTPException(status_code=400, detail="Transcription failed")
        return {"transcript": transcript.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred during transcription.")

@app.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    # //file_location = f"./downloads/{file.filename}"
    print("Uploading in the server......")
    print("file...", file)
    #file_location = f"./Users/ly/Downloads/{file.filename}"
    file_location = f"/Users/ly/Documents/Business-Projects/wordwaveapp/downloads/{file.filename}"
    #with open(file_location, "wb+") as file_object:
    with open(file_location, "wb") as file_object:    
        #file_object.write(file.file.read())
        file_object.write(await file.read())
    return JSONResponse(status_code=200, content={"message": "File saved successfully"})