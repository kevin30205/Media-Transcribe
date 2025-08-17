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

## Project Architecture

```text
Media-Transcribe/
├── data/                              # Place your input audio files here
├── output_results/                    # Transcription outputs
├── configurations/                    # YAML config files
│   ├── custom_configs/
│   │   ├── empty.yaml
│   │   ├── english/
│   │   │   └── en_config.yaml
│   │   └── traditional_chinese/
│   │       └── zh-tw_config.yaml
│   └── default_config.yaml
├── scripts/
│   └── environment_setup.sh           # Environment setup scripts
├── utils/                             # Utility modules
│   ├── basic_utils.py
│   └── logger.py
├── LICENSE
├── README.md
└── run.py                             # Main entry point
```

---

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Conda (recommended for environment management)

### Installation

```bash
# conda environment
conda create --name Media-Transcribe python=3.10.0 -y
conda activate Media-Transcribe

# required packages
pip install faster-whisper
conda install -c conda-forge hydra-core -y
conda install -c conda-forge loguru -y
```

You may also run the bash script for installation:

```bash
bash scripts/environment_setup.sh
```

---

## Usage

1. Place your media file (e.g., `audio.mp3`) in the `./data` folder.
2. Adjust configuration in `default_config.yaml` or use a custom YAML file.
3. Run transcription with one of the following commands:

```bash
# Run with default configs
python run.py

# Modify specific config (e.g., filename)
python run.py exp_setting.filename="audio.mp3"

# Use custom config YAML file
python run.py custom_configs=english/en_config

# Combine custom filename and config
python run.py exp_setting.filename="audio.mp3" custom_configs=english/en_config
```

* Any parameters specified in the command will overwrite the default configs.

* Outputs will be saved in `./output_results`.

* For more configuration options, please refer to `configurations/default_config.yaml`.

---
