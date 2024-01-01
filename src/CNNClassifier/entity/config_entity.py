from dataclasses import dataclass
from pathlib import Path

## For Data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

## For Base model 
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str 
    params_classes: int


## For Callbacks
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: str(Path)
    tensorboard_root_log_dir: str(Path)
    checkpoint_model_filepath: str(Path)