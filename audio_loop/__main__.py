"""Play an audio file in a loop with pyaudio."""
import pygame


AUDIO_FILE = "data/test.wav"
# AUDIO_FILE = "data/wnl-5s.wav"
def main():
    pygame.init()

    sound = pygame.mixer.Sound(AUDIO_FILE)
    while True:
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

if __name__ == "__main__":
    main()