from fileLocationFinder import file_location
from fastapi import APIRouter, Depends
from fastapi import File, UploadFile
from fileLocationFinder import file_location
from fastapi.responses import JSONResponse

router = APIRouter()

# Dictionary to store file path against original filename
file_path_dict = {}

@router.post("/upload/")
async def upload_audio(file: UploadFile = File(...),file_location: str = Depends(file_location)):
    # //file_location = f"./downloads/{file.filename}"
    print("Uploading in the server......")
    print("file...", file_location)
    #file_location = f"/Users/ly/Documents/Business-Projects/wordwaveapp/downloads/{file.filename}"
    
    with open(file_location, "wb") as file_object:    
        file_object.write(await file.read())
    #file_path_dict[file.filename] = file_url
    print("file_name........",file.filename)
    return JSONResponse(status_code=200, content={"message": "File saved successfully"})


