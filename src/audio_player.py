import pygame
import time
import logging
import os
import sys
import contextlib

@contextlib.contextmanager
def suppress_stderr():
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stderr = old_stderr

class AudioPlayer:
    def __init__(self, audio_file: str):
        self.audio_file = audio_file
        # Suppress unwanted stderr output during mixer initialization
        with suppress_stderr():
            pygame.mixer.init()
        logging.info("Pygame mixer initialized.")

    def play(self):
        try:
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
            logging.info(f"Playing audio: {self.audio_file}")

            # Wait until playback finishes
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            logging.info("Playback finished.")
        except Exception as e:
            logging.error(f"Error during audio playback: {e}")

# Example usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    player = AudioPlayer("audio_file/output.mp3")
    player.play()
