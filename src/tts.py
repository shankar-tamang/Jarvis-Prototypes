from gtts import gTTS


def speech_Lancer(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio_file/output.mp3")
    print("Audio saved as output.mp3")

if __name__ == "__main__":
    
    speech_Lancer("Hi, Shankar")
    