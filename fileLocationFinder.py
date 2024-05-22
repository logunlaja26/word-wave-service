from fastapi import UploadFile, File

def file_location(file: UploadFile = File(...)):
    return f"/Users/ly/Documents/Business-Projects/wordwaveapp/downloads/{file.filename}"
