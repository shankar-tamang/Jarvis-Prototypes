from gtts import gTTS
import logging

class TextToSpeech:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate(self, text):
        tts_obj = gTTS(text=text, lang='en')
        tts_obj.save("audio_file/output.mp3")
        logging.info("Audio saved as output.mp3")


    