import pygame

pygame.mixer.init()

def play_audio():
    pygame.mixer.music.load("audio_file/output.mp3")
    pygame.mixer.music.play()
    # input("Press Enter to stop playback")
    pygame.mixer.music.stop()
