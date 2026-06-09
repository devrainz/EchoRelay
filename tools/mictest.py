import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    level = np.max(np.abs(indata))
    print(f"\rLevel: {level:.5f}", end="")

print("Speak into the microphone. Ctrl+C to stop.")

with sd.InputStream(channels=1, callback=callback):
    while True:
        sd.sleep(100)