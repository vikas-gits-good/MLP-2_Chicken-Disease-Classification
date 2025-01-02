import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """Read YAML file and return data

    Args:
        file_path (Path): Path like input

    Raises:
        ValueError: if YAML file is empty
        e: Error reading YAML file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} read successfully")
            return ConfigBox(content)
    except BoxValueError:
        logger.info("Error: YAML file is empty")
        raise ValueError("Error: YAML file empty")
    except Exception as e:
        logger.info(f"Error in common.py: {e}")
        raise e


@ensure_annotations
def create_directories(dir_paths: list, verbose: bool = True):
    """Create a list of directorues

    Args:
        dir_paths (list[Path]): list of path directories
        verbose (bool, optional): Print directory creation to logs. Defaults to True.
    """
    for path in dir_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: '{path}'")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save JSON data to file

    Args:
        path (Path): path to save location
        data (dict): data to save
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file was saved at '{path}'")


@ensure_annotations
def load_josn(path: Path) -> ConfigBox:
    """load JSON file data

    Args:
        path (Path): path to JSON file to open

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from '{path}'")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save Binary files

    Args:
        data (Any): data to be saved as binaries
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file was saved at '{path}'")


@ensure_annotations
def load_bin(path: Path):
    """Load Binary files

    Args:
        path (Path): path to binary file

    Returns:
        Any: data from binary file
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary file loaded successfully from '{path}'")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB

    Args:
        path (Path): path to file

    Returns:
        str: file size of read file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def decodeImage(imgstr, file_name):
    """Decodes the image and saves it

    Args:
        imgstr (str): Image String
        file_name (Path): Path of the image
    """
    img_data = base64.b64decode(imgstr)
    with open(file_name, "wb") as f:
        f.write(img_data)
        f.close()


@ensure_annotations
def encImgtoBase64(img_path):
    """Encodes image

    Args:
        img_path (Path): Path to image file to encode

    Returns:
        Any: Encoded image
    """
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read())
