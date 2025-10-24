import os

def get_files_info(working_directory, directory="."):
    # Create the full path by joining working_directory and directory
    full_path = os.path.join(working_directory, directory)
    
    # Resolve the absolute paths to handle any relative path components
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(full_path)
    
    # Validate that the target directory is within the working directory boundaries
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check if the target path exists and is a directory
    if not os.path.exists(abs_target_dir):
        return f'Error: "{directory}" does not exist'
    
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    
    # If validation passes, get directory contents and build the output string
    try:
        items = os.listdir(abs_target_dir)
        items.sort()  # Sort for consistent output
        
        output_lines = []
        for item in items:
            try:
                item_path = os.path.join(abs_target_dir, item)
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                
                output_lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except (OSError, IOError) as e:
                # If we can't get info for a specific item, skip it but continue with others
                output_lines.append(f"- {item}: Error: {e}")
        
        return "\n".join(output_lines)
    
    except PermissionError:
        return f'Error: Permission denied accessing "{directory}"'
    except OSError as e:
        return f'Error: {e}'
    except Exception as e:
        return f'Error: {e}'
