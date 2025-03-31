from src.orchestrator import llm
from src.stt import speech_recognizer
from src.tts import speech_Lancer
from src.audio_player import play_audio


while True:
    
    speaker_text = speech_recognizer()

    response = llm.invoke(speaker_text).content

    speech_Lancer(response)


    # Specify the path to your audio file
    audio_file = "audio_file/output.mp3"

    # Play the audio file
    play_audio()



