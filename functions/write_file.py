import os
import os.path
from pathlib import Path


def write_file(working_directory, file_path, content):
    try:
        abs_path_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_path_working_directory):
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        
        # Write content to file
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
        
    except Exception as e:
        return f"Error: {str(e)}"