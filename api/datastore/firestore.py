import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('/Users/ly/Documents/Business-Projects/wordwaveapp/backend-service/word-wave-app-firebase-adminsdk-rdzqd-235e8812b5.json')
app = firebase_admin.initialize_app(cred , {
    'storageBucket': 'word-wave-app.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()


def add_update_user(user_id, username, email):
    user_ref = db.collection("Users").document(user_id)
    user_ref.set({
        'userInfo': {
            'username': username,
            'email': email
        }
    }, merge=True)
    print('Document ID: {}'.format(user_ref.id))
    
    
    
def add_update_note(user_id, note_id, title, content, created_on, last_modified):
    note_ref = db.collection('Users').document(user_id).collection('Notes').document(note_id)
    note_ref.set({
        'title': title,
        'content': content,
        'createdOn': created_on,
        'lastModified': last_modified,
        'audioBlobs': []  # Initialize empty or with existing paths
    }, merge=True)
    print(f"Note updated for {note_id} under user {user_id}")
 
    
    
def add_update_audio_blob(user_id, audio_id, filename, path, uploaded_on, size):
    audio_ref = db.collection('Users').document(user_id).collection('AudioBlobs').document(audio_id)
    audio_ref.set({
        'filename': filename,
        'path': path,
        'uploadedOn': uploaded_on,
        'size': size
    }, merge=True)
    print(f"Audio blob {filename} updated for user {user_id}")
    
 
    
def link_audio_to_note(user_id, note_id, audio_paths):
    note_ref = db.collection('Users').document(user_id).collection('Notes').document(note_id)
    note_ref.update({
        'audioBlobs': firestore.ArrayUnion(audio_paths)
    })
    print(f"Audio blobs linked to note {note_id}")
    
    
    


# Add/Update a User
add_update_user('testUserId', 'testuser', 'testuser@example.com')


# Add/Update a Note
add_update_note('testUserId', 'noteId', 'Meeting Summary',
                'Here is a detailed summary of the meeting held on...', 
                '2024-04-01T10:00:00Z', '2024-04-01T15:00:00Z')

# Manage Audio Blob
add_update_audio_blob('testUserId', 'audioId', 'audio1.mp3', 
                      'path/to/audio1.mp3', '2024-04-01T10:00:00Z', '2MB')

# Link Audio Blobs to a Note
link_audio_to_note('testUserId', 'noteId', 
                   ['path/to/audio1.mp3', 'path/to/audio2.mp3'])


blob = bucket.blob("audio_file.mp3")
blob.upload_from_filename("/Users/ly/Documents/Business-Projects/wordwaveapp/downloads/2bade4f1-eaa4-409c-ae90-399f1de0aec4-filename.mp3")

# Get a public URL for the file
public_url = blob.public_url

def audio_url():
    return public_url

# Print the public URL
print("public url: ",public_url)

# Get the object
#object = bucket.get_object('audio_file.mp3')
object = bucket.get_blob('audio_file.mp3')

