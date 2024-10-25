import click
from colorama import Fore, Style, init
from .os_info import SYSTEM_INFO
from openai import OpenAI
import os

# Initialize colorama for color support across platforms
init(autoreset=True)

# Load OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set up OpenAI API client with the loaded key
client = OpenAI(api_key=api_key)

system_prompt = "You are a terminal assistant. The user will provide a prompt, and you will respond with a single command in the format:[your_command_here]\nRespond only in this format without any additional text."

@click.command()
@click.argument('prompt', nargs=-1)  # Allows multiple arguments
def cli(prompt):
    if len(prompt) != 1:
        # Print error message in red for incorrect format if argument count is not exactly 1
        print(Fore.RED + "Incorrect format. Please use: pllm 'your prompt request'")
    else:
        user_prompt = prompt[0]
        
        # Call OpenAI's ChatCompletion API with a custom system message
        completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
            ]
        )
        
        print(Fore.LIGHTGREEN_EX + completion.choices[0].message.content.strip().strip("[]"))

if __name__ == "__main__":
    cli()
