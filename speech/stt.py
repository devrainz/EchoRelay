from faster_whisper import WhisperModel

model = WhisperModel(
    "tiny",
    device="cpu"
)

def transcribe(path):
    segments, _ = model.transcribe(path)

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()