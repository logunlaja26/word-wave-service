import assemblyai as aai

# Replace with your API key
aai.settings.api_key = ""

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
# FILE_URL = "/Users/ly/Downloads/Burna-BoyxByron-Messia-Talibans-II.mp3"


def transcribe_audio(file_url):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_url)
    if transcript.status == aai.TranscriptStatus.error:
        print(transcript.error)
    else:
        print("Transcription Status: " + transcript.status)
        print(transcript.text)
    return transcript
