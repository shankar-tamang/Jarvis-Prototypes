from Orchestrator import llm
from STT import speech_recognizer
from TTS import speech_Lancer
from Play_audio import play_audio


while True:
    
    speaker_text = speech_recognizer()

    response = llm.invoke(speaker_text).content

    speech_Lancer(response)


    # Specify the path to your audio file
    audio_file = "audio_file/output.mp3"

    # Play the audio file
    play_audio()



