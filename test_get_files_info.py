import os
import shutil
from functions.get_files_info import get_files_info

def test_get_files_info():
    # Setup test directory structure
    test_dir = "test_get_files_info_dir"
    os.makedirs(os.path.join(test_dir, "pkg"), exist_ok=True)
    
    # Create test files
    test_files = {
        "file1.txt": "Test content 1",
        "file2.txt": "Another test file",
        "pkg/module.py": "def hello():\n    return 'hello'"
    }
    
    try:
        # Create test files
        for path, content in test_files.items():
            with open(os.path.join(test_dir, path), 'w') as f:
                f.write(content)
        
        # Test 1: Current directory
        result = get_files_info(test_dir, ".")
        print("Result for current directory:")
        print(result)
        print()
        
        # Test 2: Subdirectory
        result = get_files_info(test_dir, "pkg")
        print("Result for 'pkg' directory:")
        print(result)
        print()
        
        # Test 3: Outside working directory (should fail)
        result = get_files_info(test_dir, "/bin")
        print("Result for '/bin' directory:")
        print(result)
        print()
        
        # Test 4: Parent directory (should fail)
        result = get_files_info(test_dir, "../")
        print("Result for '../' directory:")
        print(result)
        
    finally:
        # Cleanup
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_get_files_info()
