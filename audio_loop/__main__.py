"""Play an audio file in a loop with pyaudio."""
from pathlib import Path
import wave
import pyaudio

# AUDIO_FILE = "data/white-noise-loop.wav"
# AUDIO_FILE = "data/test.wav"
AUDIO_FILE = "data/wnl-5s.wav"
def main():
    audio_path = AUDIO_FILE

    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()
    with wave.open(audio_path, "rb") as wf:
        # Open stream (2)
        while True:
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

            # Play samples from the wave file (3)
            CHUNK = 1024
            while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                stream.write(data)
            wf.rewind()

            # Close stream (4)
            stream.close()

    # Release PortAudio system resources (5)
    p.terminate()

if __name__ == "__main__":
    main()