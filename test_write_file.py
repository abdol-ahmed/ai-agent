import os
import tempfile
import shutil
from functions.write_file import write_file

def test_write_file():
    # Setup test directory
    test_dir = "test_write_file_dir"
    os.makedirs(test_dir, exist_ok=True)
    
    try:
        # Test 1: Write to a file in the working directory
        content = "wait, this isn't lorem ipsum"
        result = write_file(test_dir, "lorem.txt", content)
        print(f"{len(content)} characters written")
        
        # Test 2: Write to a file in a subdirectory (should create the directory)
        content = "lorem ipsum dolor sit amet"
        result = write_file(test_dir, "pkg/morelorem.txt", content)
        print(f"{len(content)} characters written")
        
        # Test 3: Attempt to write outside working directory (should fail)
        result = write_file(test_dir, "/tmp/temp.txt", "this should not be allowed")
        print("Error:", result)
        
    finally:
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_write_file()
