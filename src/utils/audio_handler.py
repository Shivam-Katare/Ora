def save_audio_to_file(base64_audio, filename):
    import base64
    import os

    # Ensure the audio directory exists
    audio_dir = os.path.join(os.path.dirname(__file__), '../static/audio')
    os.makedirs(audio_dir, exist_ok=True)

    # Define the full path for the audio file
    file_path = os.path.join(audio_dir, filename)

    # Decode the base64 audio and write to file
    with open(file_path, 'wb') as audio_file:
        audio_file.write(base64.b64decode(base64_audio))

    return file_path

def load_audio_file(filename):
    import os

    # Define the full path for the audio file
    file_path = os.path.join(os.path.dirname(__file__), '../static/audio', filename)

    if os.path.exists(file_path):
        return file_path
    else:
        return None