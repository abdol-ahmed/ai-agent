import os
import os.path
from pathlib import Path

from google.genai import types


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

def schema_write_file():
    return types.FunctionDeclaration(
	    name="write_file",
	    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
	    parameters=types.Schema(
		    type=types.Type.OBJECT,
		    properties={
			    "file_path": types.Schema(
				    type=types.Type.STRING,
				    description="Path to the file to write, relative to the working directory.",
			    ),
			    "content": types.Schema(
				    type=types.Type.STRING,
				    description="Content to write to the file",
			    ),
		    },
		    required=["file_path", "content"],
	    ),
    )