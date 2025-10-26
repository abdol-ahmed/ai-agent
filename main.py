import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import MODEL_NAME, SYSTEM_PROMPT, WORKING_DIR
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file


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

	if not api_key:
		print("Error: GEMINI_API_KEY environment variable not set.")
		sys.exit(1)

	client = genai.Client(api_key=api_key)

	# Maximum number of iterations to prevent infinite loops
	max_iterations = 20
	iteration = 0

	try:
		while iteration < max_iterations:
			if verbose:
				print(f"\n--- Iteration {iteration + 1}/{max_iterations} ---")

			# Get the response from the model
			response = generate_content(client, messages, verbose)

			# Check if we have a final text response
			if response:
				print("Final response:")
				print(response)
				break

			iteration += 1
		else:
			print("\nReached maximum number of iterations. Stopping.")
			sys.exit(1)

	except KeyboardInterrupt:
		print("\nOperation cancelled by user.")
		sys.exit(0)
	except Exception as e:
		print(f"\nAn error occurred: {str(e)}")
		if verbose:
			import traceback
			traceback.print_exc()
		sys.exit(1)


def generate_content(client, messages, verbose=False):
	if verbose:
		print("\n--- Sending to model ---")
		print(f"Messages: {messages}")

	try:
		response = client.models.generate_content(
			model="gemini-2.0-flash-001",
			contents=messages,
			config=types.GenerateContentConfig(
				tools=[get_available_functions()],
				system_instruction=SYSTEM_PROMPT
			),
		)

		if verbose:
			print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
			print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

		# Process the model's response
		if response.candidates:
			for candidate in response.candidates:
				# Add the model's response to messages
				messages.append(candidate.content)

		# Check if there are function calls to process
		if not response.function_calls:
			return response.text

		# Process function calls if any
		function_responses = []
		for function_call_part in response.function_calls:
			function_call_result = call_function(function_call_part, verbose=verbose)

			if (not function_call_result.parts or not function_call_result.parts[0].function_response):
				raise Exception("empty function call result")

			if verbose:
				print(f"-> {function_call_result.parts[0].function_response.response}")

			function_responses.append(function_call_result.parts[0])

		if not function_responses:
			raise Exception("no function responses generated, exiting.")

		# Convert function responses to a user message and add to messages
		function_message = types.Content(
			role="user",
			parts=function_responses
		)
		messages.append(function_message)
	except Exception as e:
		print(f"\nError in generate_content: {str(e)}")
		if verbose:
			import traceback
			traceback.print_exc()
		# Re-raise the exception to be handled by the main loop
		raise


# Create the available functions tool
def get_available_functions():
	return types.Tool(
		function_declarations=[
			schema_get_files_info(),
			schema_get_file_content(),
			schema_run_python_file(),
			schema_write_file(),
		]
	)

def call_function(function_call_part, verbose=False):
	function_name = function_call_part.name
	function_args = dict(function_call_part.args) or {}

	# Map of available functions
	available_functions = {
		"get_files_info": get_files_info,
		"get_file_content": get_file_content,
		"write_file": write_file,
		"run_python_file": run_python_file
	}

	if verbose:
		print(f" - Calling function: {function_name}({function_args})")
	else:
		print(f" - Calling function: {function_name}")

	# Check if function exists
	if function_name not in available_functions:
		return types.Content(
			role="tool",
			parts=[
				types.Part.from_function_response(
					name=function_name,
					response={"error": f"Unknown function: {function_name}"},
				)
			],
		)

	# Add working directory to function arguments
	function_args["working_directory"] = WORKING_DIR

	try:
		# Call the function with the provided arguments
		function = available_functions[function_name]
		result = function(**function_args)

		# Convert the result to the appropriate format
		return types.Content(
			role="tool",
			parts=[
				types.Part.from_function_response(
					name=function_name,
					response=result if isinstance(result, dict) else {"result": result},
				)
			],
		)
	except Exception as e:
		return types.Content(
			role="tool",
			parts=[
				types.Part.from_function_response(
					name=function_name,
					response={"error": f"Error calling function {function_name}: {str(e)}"},
				)
			],
		)

if __name__ == "__main__":
	main()