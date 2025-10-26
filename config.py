"""
Configuration module for the AI Agent project.
Centralizes all project settings and configuration values.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Main configuration class for the AI Agent project."""
    
    # Project metadata
    PROJECT_NAME = "ai-agent"
    VERSION = "0.1.0"
    DESCRIPTION = "AI Agent with calculator and file system utilities"
    
    # API Configuration
    GEMINI_API_KEY: Optional[str] = os.environ.get("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.0-flash-001"  # Updated to a valid Gemini model name
    ##SYSTEM_PROMPT = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
    WORKING_DIR = "./calculator"
    SYSTEM_PROMPT = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
	- Read file contents
	- Execute Python files with optional arguments
	- Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    # File System Configuration
    MAX_FILE_SIZE = 10000  # Maximum characters to read from a file
    DEFAULT_WORKING_DIRECTORY = os.getcwd()
    TIMEOUT = 30  # Default timeout in seconds for subprocess execution
    
    # Calculator Configuration
    CALCULATOR_PRECISION = 10  # Decimal precision for calculations
    
    # Logging Configuration
    VERBOSE_MODE = False
    LOG_LEVEL = "INFO"
    
    # Security Configuration
    ALLOWED_FILE_EXTENSIONS = ['.py', '.txt', '.md', '.json', '.yaml', '.yml', '.toml']
    MAX_DIRECTORY_DEPTH = 10  # Maximum directory traversal depth
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that all required configuration is present."""
        if not cls.GEMINI_API_KEY:
            print("Warning: GEMINI_API_KEY not found in environment variables")
            return False
        return True
    
    @classmethod
    def get_model_config(cls) -> dict:
        """Get model-specific configuration."""
        return {
            "model": cls.GEMINI_MODEL,
            "api_key": cls.GEMINI_API_KEY
        }
    
    @classmethod
    def get_file_config(cls) -> dict:
        """Get file system configuration."""
        return {
            "max_file_size": cls.MAX_FILE_SIZE,
            "working_directory": cls.DEFAULT_WORKING_DIRECTORY,
            "allowed_extensions": cls.ALLOWED_FILE_EXTENSIONS,
            "max_directory_depth": cls.MAX_DIRECTORY_DEPTH
        }
    
    @classmethod
    def get_calculator_config(cls) -> dict:
        """Get calculator configuration."""
        return {
            "precision": cls.CALCULATOR_PRECISION
        }


class DevelopmentConfig(Config):
    """Development-specific configuration."""
    VERBOSE_MODE = True
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    """Production-specific configuration."""
    VERBOSE_MODE = False
    LOG_LEVEL = "WARNING"


def get_config(environment: str = "development") -> Config:
    """Get configuration based on environment."""
    config_map = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "default": Config
    }
    return config_map.get(environment, Config)()


# Environment-specific configuration
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
config = get_config(ENVIRONMENT)

# Export commonly used values for convenience
API_KEY = config.GEMINI_API_KEY
MODEL_NAME = config.GEMINI_MODEL
MAX_FILE_CHARS = config.MAX_FILE_SIZE
DEFAULT_WORKING_DIR = config.DEFAULT_WORKING_DIRECTORY
SYSTEM_PROMPT = config.SYSTEM_PROMPT
WORKING_DIR = config.WORKING_DIR