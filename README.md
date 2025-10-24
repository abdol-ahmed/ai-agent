# AI Agent Project

A comprehensive Python project demonstrating AI integration, mathematical computation, and file system utilities. This project showcases modern Python development practices, API integration, and modular architecture.

## 🚀 Features

### 1. **AI Agent with Google Gemini Integration**
- Interactive AI chat using Google's Gemini API
- Command-line interface with verbose mode
- Token usage tracking and monitoring
- Environment-based configuration management

### 2. **Advanced Calculator Engine**
- Infix expression evaluation with operator precedence
- Support for basic arithmetic operations (+, -, *, /)
- JSON-formatted output
- Comprehensive error handling and validation

### 3. **File System Utilities**
- Secure file content reading with size limits
- Directory listing with metadata
- Path validation and security checks
- Cross-platform compatibility

### 4. **Python File Execution**
- Safe execution of Python files with controlled environment
- Secure path validation to prevent directory traversal
- Timeout protection for long-running scripts
- Clean output formatting with STDOUT/STDERR separation
- Comprehensive error handling with descriptive messages

### 4. **Configuration Management**
- Environment-based configuration
- Centralized settings management
- Development/Production environment separation
- Type-safe configuration with validation

## 📁 Project Structure

```
ai-agent/
├── main.py                 # AI Agent main entry point
├── config.py              # Centralized configuration
├── pyproject.toml         # Project dependencies and metadata
├── calculator/            # Calculator module
│   ├── main.py            # Calculator CLI
│   ├── pkg/
│   │   ├── calculator.py  # Core calculator logic
│   │   └── render.py      # JSON output formatting
│   └── tests.py           # Calculator unit tests
├── functions/             # Utility functions
│   ├── get_file_content.py # File reading functions
│   ├── get_files_info.py  # Directory listing functions
│   └── run_python_file.py # Python file execution
└── tests.py              # Integration tests
```

## 🛠️ Installation

### Prerequisites
- Python 3.12+
- Google Gemini API key

### Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -e .
   # or using uv (recommended)
   uv sync
   ```

3. **Set up environment variables:**
   ```bash
   # Create a .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   echo "ENVIRONMENT=development" >> .env
   ```

## 🎯 Usage Examples

### 1. AI Agent
```bash
# Basic AI interaction
python main.py "What is the capital of France?"

# Verbose mode with token tracking
python main.py --verbose "Explain quantum computing"
```

**Output:**
```
User prompt: Explain quantum computing
Prompt tokens: 15
Response tokens: 150
[AI Response...]
```

### 2. Calculator
```bash
# Basic arithmetic
python calculator/main.py "3 + 5 * 2"

# Complex expressions
python calculator/main.py "2 * 3 - 8 / 2 + 5"
```

**Output:**
```json
{
  "expression": "2 * 3 - 8 / 2 + 5",
  "result": 7
}
```

### 3. File System Utilities
```python
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

# Read file content
content = get_file_content("calculator", "main.py")
print(content)

# List directory contents
files_info = get_files_info("calculator", "pkg")
print(files_info)
```

### 4. Configuration Management
```python
from config import config, get_config

# Access configuration
api_key = config.GEMINI_API_KEY
max_file_size = config.MAX_FILE_SIZE

# Environment-specific config
dev_config = get_config("development")
prod_config = get_config("production")

# Validate configuration
if config.validate_config():
    print("Configuration is valid")
```

## 🧪 Testing

### Run Calculator Tests
```bash
cd calculator
python tests.py
```

### Run Integration Tests
```bash
python tests.py
```

### Test File System Functions
```bash
python -c "from tests import test_get_file_content; test_get_file_content()"
```

## 🎓 Learning Outcomes

### **1. Modern Python Development**
- **Project Structure**: Learn modular architecture with proper package organization
- **Dependency Management**: Understand `pyproject.toml` and modern Python packaging
- **Type Hints**: Practice type safety with `Optional[str]` and return type annotations
- **Environment Management**: Master `.env` files and environment-based configuration

### **2. API Integration & AI Development**
- **REST API Integration**: Learn to work with Google's Gemini API
- **Authentication**: Understand API key management and security
- **Response Handling**: Process structured API responses and metadata

### **3. Algorithm Implementation**
- **Infix Expression Evaluation**: Master the shunting yard algorithm
- **Operator Precedence**: Understand and implement precedence rules
- **Stack-based Processing**: Learn stack data structure applications
- **Mathematical Computation**: Implement safe arithmetic operations

### **4. File System Programming**
- **Path Security**: Learn to prevent directory traversal attacks
- **File I/O**: Master safe file reading with size limits
- **Cross-platform Compatibility**: Handle different OS path separators
- **Error Handling**: Implement comprehensive file system error handling

### **5. Python Execution**
- **Subprocess Management**: Safely execute Python files with subprocess
- **Output Handling**: Capture and format STDOUT/STDERR streams
- **Security**: Execute untrusted code in a controlled environment
- **Resource Management**: Set timeouts and handle process termination

## 🐍 Running Python Files

The `run_python_file.py` utility provides a secure way to execute Python files with proper output handling and error management.

### Usage

```python
from functions.run_python_file import run_python_file

# Basic usage
result = run_python_file("path/to/directory", "script.py")

# With command line arguments
result = run_python_file("path/to/directory", "script.py", ["arg1", "arg2"])

# The result is a string containing formatted output:
# - STDOUT: [output from script]
# - STDERR: [any error messages]
# - Process exit status (if non-zero)
```

### Error Handling

The function provides detailed error messages for common issues:
- File not found: `Error: File "script.py" not found`
- Permission denied: `Error: Cannot execute "script.py" as it is outside the permitted working directory`
- Invalid file type: `Error: "file.txt" is not a Python file.`
- Execution errors: `Error: executing Python file: [error details]`

### Security Features
- Prevents directory traversal attacks
- Validates file paths against working directory
- Enforces Python file extension requirement
- Implements execution timeouts

### **5. Software Architecture**
- **Configuration Management**: Design centralized configuration systems
- **Environment Separation**: Implement dev/prod environment handling
- **Modular Design**: Create reusable, testable components
- **Separation of Concerns**: Separate business logic from presentation
### **6. Testing & Quality Assurance**
- **Unit Testing**: Write comprehensive test suites with `unittest`
- **Test Organization**: Structure tests for maintainability
- **Edge Case Testing**: Test error conditions and boundary cases
- **Integration Testing**: Test component interactions

### **7. CLI Development**
- **Argument Parsing**: Handle command-line arguments and flags
- **User Experience**: Design intuitive command-line interfaces
- **Output Formatting**: Create structured, parseable output (JSON)
- **Error Messaging**: Provide clear, actionable error messages

## 🔧 Configuration Options

The project uses a sophisticated configuration system:

```python
# Development settings
ENVIRONMENT=development
VERBOSE_MODE=true
LOG_LEVEL=DEBUG

# Production settings  
ENVIRONMENT=production
VERBOSE_MODE=false
LOG_LEVEL=WARNING

# API Configuration
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.0-flash-001

# File System Limits
MAX_FILE_SIZE=10000
MAX_DIRECTORY_DEPTH=10
```

## 🚨 Security Features

- **Path Validation**: Prevents directory traversal attacks
- **File Size Limits**: Prevents memory exhaustion
- **Extension Filtering**: Restricts file types for security
- **Working Directory Enforcement**: Limits file access scope

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Dependencies

- `google-genai==1.12.1` - Google Gemini API client
- `python-dotenv==1.1.0` - Environment variable management

---

**Happy Coding! 🐍✨**

This project demonstrates real-world Python development skills including API integration, mathematical computation, file system programming, and modern software architecture patterns.
