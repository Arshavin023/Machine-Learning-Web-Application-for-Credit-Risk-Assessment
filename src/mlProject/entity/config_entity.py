from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    learning_rate: float
    n_estimators: int
    max_depth: int
    subsample: float
    colsample_bytree: float
    gamma: float
    reg_alpha: float
    reg_lambda: float
    min_child_weight: int
    eval_metric: str
    early_stopping_rounds: int
    tree_method: str
    scale_pos_weight: int
    objective: str
    target_column: str