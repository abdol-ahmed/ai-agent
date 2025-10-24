import os
import shutil
from functions.get_file_content import get_file_content

def test_get_file_content():
    # Setup test directory
    test_dir = "test_get_file_content_dir"
    os.makedirs(test_dir, exist_ok=True)
    
    # Create test files based on the original tests.py
    test_files = {
        "lorem.txt": "wait, this isn't lorem ipsum",
        "main.py": "# Sample main.py\nprint('Hello, World!')",
        "pkg/calculator.py": "def add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b"
    }
    
    try:
        # Create test files and directories
        for path, content in test_files.items():
            os.makedirs(os.path.dirname(os.path.join(test_dir, path)) or '.', exist_ok=True)
            with open(os.path.join(test_dir, path), 'w') as f:
                f.write(content)
        
        # Test 1: Read lorem.txt
        result = get_file_content(test_dir, "lorem.txt")
        print(f"{len(result)} characters read")
        
        # Test 2: Read main.py
        result = get_file_content(test_dir, "main.py")
        print(f"{len(result)} characters read")
        
        # Test 3: Read pkg/calculator.py
        result = get_file_content(test_dir, "pkg/calculator.py")
        print(f"{len(result)} characters read")
        
        # Test 4: Attempt to read /bin/cat (outside working directory)
        result = get_file_content(test_dir, "/bin/cat")
        print("Error:", result)
        
        # Test 5: Attempt to read non-existent file
        result = get_file_content(test_dir, "pkg/does_not_exist.py")
        print("Error:", result)
        
    finally:
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_get_file_content()
