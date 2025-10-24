"""Tests for the run_python_file function."""

import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import run_python_file
sys.path.append(str(Path(__file__).parent.parent))
from functions.run_python_file import run_python_file


def test_run_python_file():
    """Test various scenarios for run_python_file function."""
    print("\n=== Testing run_python_file function ===")
    
    # Test 1: Run calculator without arguments (should show help)
    result = run_python_file("calculator", "main.py")
    print(result)
    
    # Test 2: Run calculator with a simple expression
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    
    # Test 3: Run calculator's test suite
    result = run_python_file("calculator", "tests.py")
    print(result)
    
    # Test 4: Try to run a file outside working directory (should fail)
    result = run_python_file("calculator", "../main.py")
    print(result)
    
    # Test 5: Try to run a non-existent file (should fail)
    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    # Test 6: Try to run a non-Python file (should fail)
    result = run_python_file("calculator", "lorem.txt")
    print(result)
    
    print("\n=== Test completed ===")


if __name__ == "__main__":
    test_run_python_file()
