import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def connect_shell_to_gpt():
    while True:
        command = input("Enter shell command: ")
        if command.lower() in ["exit", "quit"]:
            break
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"Execute shell command: {command}",
            max_tokens=100
        )
        print(response.choices[0].text.strip())

if __name__ == "__main__":
    connect_shell_to_gpt()
