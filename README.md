# Short Drama Generative Pipeline

An end-to-end media automation compiler for mobile short dramas. Parses textual screenplay dialogues, dynamically allocates gender-specific voice characters, and automatically generates millisecond-accurate synchronized SRT subtitles alongside ComfyUI SVD video rendering.

## Core Features

- **Screenplay Dialog Parsing**: Automatically isolates dialogues and parses speaker actions from screenplay texts.
- **Bilingual Neural Voice Cloning**:
  - Uses local **Kokoro MLX** for high-speed, crisp English voiceovers.
  - Integrates **ChatTTS API** with locked-in female and male seed profiles (Seeds `313` / `2222`) for natural, expressive Chinese narration.
- **Automatic SRT Sync**: Computes word-length duration indices to generate synchronized SRT files with millisecond precision.
- **Consistent Video Generation**: Multiplexes synthesized audios with Stable Video Diffusion visual frames.

## Installation

```bash
pip install kokoro-mlx chattts pandas numpy ffmpeg-python
```

## Usage

Run the orchestrator to parse a script and export voiceovers and subtitles:

```bash
python tts_orchestrator.py
```
