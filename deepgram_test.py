from deepgram import Deepgram
import json

# The API key we created in step 3
DEEPGRAM_API_KEY = '31870ad6a4182b1006d6df399cc2036be949bebe'

# Replace with your file path and audio mimetype
PATH_TO_FILE = 'C:\\Users\\gpu20\\OneDrive\\Desktop\\JustIT\\Github\\Deepgram_voiceAI\\lightningKBOS-App-North-Sep-19-2023-0330Z.mp3'
MIMETYPE = 'audio/mpeg'

def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    
    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = { "smart_format": True, "model": "nova", "language": "en-US" }
    
        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')
        print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
        print('To learn more about customizing your transcripts check out developers.deepgram.com')
    
        response = dg_client.transcription.sync_prerecorded(source, options)
        print(json.dumps(response, indent=4))

main()