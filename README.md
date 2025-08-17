# Media Transcribe

**Media Transcribe** is a tool that uses advanced speech recognition models to automatically convert media files into text. It is suitable for note-taking, content creation, and accessibility purposes, providing a streamlined workflow for generating transcripts and subtitles from your media files.

---

## Main Features

- **Automatic Speech-to-Text:** Utilizes state-of-the-art speech recognition models to provide reliable transcription results.
- **Supported Media Formats:** Supports media files such as MP3, WAV and MP4.
- **Simple Workflow:** Place your media file in the `./data` folder, adjust the YAML configuration file as needed, and run the provided command to start transcription.
- **SRT Subtitle Output:** Automatically generates SRT subtitle files for easy use in other applications.
- **Content Generation & Accessibility:** Converts lectures, interviews, and meetings into searchable text, improving accessibility and usability.

---

## Technology Stack

- **Python** (>=3.10)
- **faster-whisper** (speech recognition)
- **hydra-core** (configuration management)
- **omegaconf** (YAML config parsing)
- **loguru** (logging)


---
