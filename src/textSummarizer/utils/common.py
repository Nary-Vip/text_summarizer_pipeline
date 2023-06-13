import os
import yaml
from typing import Any
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        ValueError: If yaml file is empty.

    Returns:
        Box: ConfigBox type.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("Yaml file contains invalid data.") from e
    except FileNotFoundError as e:
        raise ValueError(f"Yaml file '{path_to_yaml}' not found.") from e
    except Exception as e:
        raise ValueError(f"Failed to read yaml file '{path_to_yaml}'.") from e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories.

    Args:
        path_to_directories (list): List of paths to directories
        ignore_log (bool, optional): Ignore if multiple directories are to be created. Defaults to False.
        verbose (bool, optional): Log verbose output. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} kB"