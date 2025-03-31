# src/main.py

import logging
from src.orchestrator import Orchestrator
from src.stt import SpeechRecognizer
from src.tts import TextToSpeech
from src.audio_player import AudioPlayer

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    stt = SpeechRecognizer()
    tts = TextToSpeech(output_path="audio_file/output.mp3")
    orchestrator = Orchestrator()
    audio_player = AudioPlayer(audio_file="audio_file/output.mp3")

    while True:
        audio = stt.listen()
        speaker_text = stt.recognize(audio)

        # Skip if no speech is recognized
        if not speaker_text:
            continue

        # Check for the stop command to cancel the overall system
        if speaker_text.strip().lower() == "stop":
            logging.info("Stop command received. Exiting the system...")
            break

        response = orchestrator.generate(speaker_text)

        if response:
            tts.generate(response)
            audio_player.play()

if __name__ == "__main__":
    main()
