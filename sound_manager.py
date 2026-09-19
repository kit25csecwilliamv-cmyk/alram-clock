import pygame
import os

pygame.mixer.init()


def play_alarm():
    sound_file = "sounds/alarm1.mp3"

    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(-1)
    else:
        print("Alarm sound not found!")


def stop_alarm():
    pygame.mixer.music.stop()
