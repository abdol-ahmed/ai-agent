import os

from google.genai import types

from config import MAX_FILE_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_target_file_path):
        return f'Error: "{abs_target_file_path}" does not exist'
    
    if not os.path.isfile(abs_target_file_path):
        return f'Error: File not found or is not a regular file: "{abs_target_file_path}"'
    
    try:
        with open(abs_target_file_path, 'r') as file:
            content = file.read(MAX_FILE_CHARS)
            if os.path.getsize(abs_target_file_path) > MAX_FILE_CHARS:
                content += f"[...File {file_path} truncated at {MAX_FILE_CHARS} characters]"
            return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


def schema_get_file_content():
    return types.FunctionDeclaration(
        name="get_file_content",
	    description=f"Reads and returns the first {MAX_FILE_CHARS} characters of the content from a specified file within the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file whose content should be read, relative to the working directory.",
                ),
            },
	        required=["file_path"],
        ),
    )
