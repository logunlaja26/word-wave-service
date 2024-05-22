from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from transcribe import transcribe_audio
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints.upload import router as upload_router
from api.endpoints.transcribe import router as transcribe_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# file_location = ""

# @app.post("/upload/")
# async def upload_audio(file: UploadFile = File(...)):
#     # //file_location = f"./downloads/{file.filename}"
#     print("Uploading in the server......")
#     print("file...", file)
#     global file_location
#     file_location = f"/Users/ly/Documents/Business-Projects/wordwaveapp/downloads/{file.filename}"
#     with open(file_location, "wb") as file_object:    
#         file_object.write(await file.read())
#     return JSONResponse(status_code=200, content={"message": "File saved successfully"})

# @app.post("/api/transcribe")
# async def read_root():
#     global file_location
#     try:
#         transcript = transcribe_audio(file_location)
#         return {"transcript": transcript.text}
#     except Exception as e:
#         print("Error...", e)
#         raise HTTPException(status_code=500, detail="An error occurred during transcription.")

app.include_router(upload_router)
app.include_router(transcribe_router)