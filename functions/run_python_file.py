import os.path
import subprocess
from typing import List, Optional

from google.genai import types

from config import Config


def format_output(stdout: str, stderr: str, returncode: int) -> str:
    """Format the output with STDOUT/STDERR prefixes and include return code if non-zero."""
    output_parts = []
    
    if stdout:
        output_parts.append(f"STDOUT:\n{stdout}")
    if stderr:
        output_parts.append(f"STDERR:\n{stderr}")
    
    if not output_parts:
        return "No output produced."
    
    output = "\n\n".join(output_parts)
    
    if returncode != 0:
        output += f"\n\nProcess exited with code {returncode}"
    
    return output


def run_python_file(working_directory: str, file_path: str, args: Optional[List[str]] = None) -> str:
    """
    Execute a Python file and return formatted output.
    
    Args:
        working_directory: The working directory for the script
        file_path: Path to the Python file to execute (relative to working_directory)
        args: Command line arguments to pass to the script
        
    Returns:
        Formatted string containing STDOUT/STDERR and process status
    """
    if args is None:
        args = []
        
    abs_path_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Initial validations
    if not abs_file_path.startswith(abs_path_working_directory):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.exists(abs_file_path):
        return f"Error: File \"{file_path}\" not found"

    if not os.path.isfile(abs_file_path):
        return f"Error: \"{file_path}\" is not a regular file"

    if not abs_file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."

    try:
        # Run the Python file and capture the output
        process = subprocess.Popen(
            ["python", abs_file_path] + args,
            cwd=abs_path_working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        try:
            stdout, stderr = process.communicate(timeout=Config.TIMEOUT)
            return format_output(stdout, stderr, process.returncode)
            
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            return format_output(
                stdout,
                f"Process timed out after {Config.TIMEOUT} seconds\n{stderr}",
                -1
            )
        
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"

def schema_run_python_file():
    return types.FunctionDeclaration(
	    name="run_python_file",
	    description="Executes a Python file within the working directory and returns the output from the interpreter.",
	    parameters=types.Schema(
		    type=types.Type.OBJECT,
		    properties={
			    "file_path": types.Schema(
				    type=types.Type.STRING,
				    description="Path to the Python file to execute, relative to the working directory.",
			    ),
			    "args": types.Schema(
				    type=types.Type.ARRAY,
				    items=types.Schema(
					    type=types.Type.STRING,
					    description="Optional arguments to pass to the Python file.",
				    ),
				    description="Optional arguments to pass to the Python file.",
			    ),
		    },
		    required=["file_path"],
	    ),
    )