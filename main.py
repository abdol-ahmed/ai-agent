import os
import sys
from dotenv import load_dotenv 
from google import genai
from google.genai import types


def main():
    load_dotenv()
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Error: A prompt argument is required.")
        sys.exit(1)
    
    # Check for --verbose flag
    verbose = False
    args = sys.argv[1:]
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")  # Remove the flag from args
    
    if not args:  # No prompt after removing --verbose
        print("Error: A prompt argument is required.")
        sys.exit(1)
    
    prompt = " ".join(args)  # Join remaining arguments

    if verbose:
        print(f"User prompt: {prompt}")
    
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        ),
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    generate_content(client, messages, verbose)
    

def generate_content(client, messages, verbose=False):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    


if __name__ == "__main__":
    main()