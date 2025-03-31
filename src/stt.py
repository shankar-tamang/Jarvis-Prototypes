import speech_recognition as sr
import logging

class SpeechRecognizer():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            logging.info("Listening for speech...")
            audio = self.recognizer.listen(source)

        return audio
    
    def recognize(self, audio):
        try: 
            text = self.recognizer.recognize_google(audio)
            logging.info(f"Recgnized speech: {text}")
            return text
        except sr.UnknownValueError:
            logging.warning("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            logging.error(f"Request error: {e}")
            return None

