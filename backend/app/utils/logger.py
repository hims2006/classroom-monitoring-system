"""Logging Setup"""

import logging
import os
from app.config import get_settings

settings = get_settings()


def setup_logger(name: str = "classroom_monitoring") -> logging.Logger:
    """Setup application logger"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.log_level))
    
    log_dir = os.path.dirname(settings.log_file)
    os.makedirs(log_dir, exist_ok=True)
    
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(getattr(logging, settings.log_level))
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, settings.log_level))
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
