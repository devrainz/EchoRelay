import json

from audio import start_recording
from audio import stop_recording

with open("config.json") as f:
    config = json.load(f)

proc = start_recording(
    "recording.wav",
    config["linux_input_source"]
)

input("Press ENTER to stop\n")

stop_recording(proc)

print("Done")