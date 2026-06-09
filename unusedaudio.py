import sounddevice as sd
import soundfile as sf

def record_audio(filename="recording.wav"):
    samplerate = 48000

    print("Recording for 5 seconds...")

    audio = sd.rec(
        int(5 * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32",
        device=(12, None)  # pulse
    )

    sd.wait()

    sf.write(filename, audio, samplerate)

    print(f"Saved to {filename}")