import pyaudio
import numpy as np

SAMPLE_RATE = 44100
FREQUENCY = 440
DURATION = 2
VOLUME = 0.5

time = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
wave = (np.sin(2 * np.pi * FREQUENCY * time) * VOLUME * 32767).astype(np.int16)

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=SAMPLE_RATE,
    output=True
)

stream.write(wave.tobytes())

stream.stop_stream()
stream.close()
p.terminate()