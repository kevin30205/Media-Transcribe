import hydra
from omegaconf import DictConfig, OmegaConf
import os

from utils.logger import Logger
from utils.basic_utils import format_timestamp

from faster_whisper import WhisperModel


@hydra.main(version_base=None, config_path="configurations", config_name="default_config")
def run(configs: DictConfig) -> None:
    """
    create logger
    """
    logger = Logger(configs=configs)
    logger.info(f"Start Implementing the Process...")

    """
    Save configs
    """
    # save configs to yaml file
    config_path = os.path.join(configs.exp_setting.exp_dir, "configs", "configs.yaml")
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    OmegaConf.save(configs, config_path)
    
    # convert configs to yaml
    configs_yaml = OmegaConf.to_yaml(configs, resolve=True)

    # get the filename of the target audio file
    audio_file_name_with_extension = os.path.basename(configs.WhisperModel.transcribe.audio)
    audio_file, _ = os.path.splitext(audio_file_name_with_extension)

    # Extract the WhisperModel section configuration
    init_config = configs.WhisperModel.init
    transcribe_config = configs.WhisperModel.transcribe

    """
    core process
    """
    logger.info(f"Start Creating Network...")
    model = WhisperModel(
        **init_config,
    )
    logger.info(f"Finsihed Creating Network...")

    # output of the model
    segments, info = model.transcribe(
        **transcribe_config,
    )

    logger.info(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")

    # Save results to SRT file
    srt_file_path = os.path.join(configs.exp_setting.exp_dir, "transcription", f"{audio_file}.srt")
    os.makedirs(os.path.dirname(srt_file_path), exist_ok=True)

    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            logger.info(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

            # convert the format to "HH:MM:SS,mmm"
            start_time = format_timestamp(segment.start)
            end_time = format_timestamp(segment.end)
            text = segment.text.strip()
            
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")
            
            # flush the buffer to ensure that the data is written to the file
            srt_file.flush()

