# EchoRelay

Push-to-talk voice relay for Windows and Linux. Speak into your mic, get clean synthesized audio back through a virtual microphone — in real time.

EchoRelay transcribes what you say, fixes the grammar, runs it through a TTS engine, and routes the result to a virtual mic so other apps pick it up as if it were you talking normally without actually exposing your real voice.

---

## What it does

- **Push-to-talk capture** — hold a hotkey, speak, release. That's the whole flow.
- **Speech-to-text transcription** — your voice gets converted to text
- **Grammar correction** — the transcription gets cleaned up before it hits the TTS
- **TTS synthesis** — corrected text is spoken back through your chosen engine
- **Virtual microphone output** — the audio routes to a virtual mic, usable in any app

---

## TTS Engines

Three engines are planned, each with a different tradeoff:

| Engine | Type | Notes |
|---|---|---|
| **gTTS** | Google Translate TTS | Lightweight, broad language support |
| **Edge Neural TTS** | Microsoft Edge neural voices | High quality, natural-sounding |
| **Piper Voices TTS** | Local neural TTS | Fully offline, low latency |

---

## Platform support

- **Linux** — PipeWire / PulseAudio virtual sink routing
- **Windows** — VB-Cable or similar virtual audio cable

---

## Status

Current state considered as work in progress. Core pipeline is being built out — transcription → correction → synthesis → routing. TTS engine switching and config will come once the base is stable.