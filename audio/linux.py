import subprocess

def start_recording(filename, source):
    return subprocess.Popen([
        "parecord",
        "--device", source,
        "--rate", "16000",
        "--channels", "1",
        filename
    ])

def stop_recording(proc):
    proc.terminate()
    proc.wait()