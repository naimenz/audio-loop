"""Play an audio file in a loop with pygame."""
import pygame
import os
import fire

def audio_loop(audio_path: str):
    pygame.mixer.init()

    # Set the desired volume (0.0 to 1.0)
    volume = 0.5
    paused = False

    # Load the WAV file
    sound = pygame.mixer.Sound(audio_path)
    sound.set_volume(volume)

    # Start playing the WAV file
    sound.play(-1)  # -1 means loop indefinitely

    while True:
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Increase volume
                    volume = min(volume + 0.1, 1.0)
                    sound.set_volume(volume)
                elif event.key == pygame.K_DOWN:
                    # Decrease volume
                    volume = max(volume - 0.1, 0.0)
                    sound.set_volume(volume)
                elif event.key == pygame.K_SPACE:
                    # Toggle pause/play
                    if paused:
                        pygame.mixer.unpause()
                        paused = False
                    else:
                        pygame.mixer.pause()
                        paused = True
                elif event.key == pygame.K_q:
                    # Quit the script
                    pygame.quit()
                    os._exit(0)
def main():
    fire.Fire(audio_loop)