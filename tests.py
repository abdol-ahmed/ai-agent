import importlib.util
from pathlib import Path

# Configuration: List of test modules to run
TEST_MODULES = [
    "test_write_file",
    "test_get_file_content",
    "test_get_files_info",
    "test_run_python_file"
    # Add new test modules here
]

def run_test_module(module_name):
    """Dynamically import and run a test module."""
    try:
        print(f"\n{'='*50}")
        print(f"Running tests in {module_name}...")
        print("="*50)
        
        # Import the test module
        spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Run the test function
        test_func = getattr(module, module_name)
        test_func()
        
    except Exception as e:
        print(f"Error running {module_name}: {e}")
        return False
    return True

def main():
    # Run all configured test modules
    for module_name in TEST_MODULES:
        run_test_module(module_name)

if __name__ == "__main__":
    main()

