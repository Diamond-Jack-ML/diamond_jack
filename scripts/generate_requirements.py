import openai
import os
import json

def get_requirements_from_gpt(file_structure):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Prepare the prompt with the file structure content
    prompt = (
        "Given the following project file structure, generate a requirements.txt file with the most current versions of the necessary dependencies. "
        "Please do not include any additional explanations. Simply output the requirements.txt file for the technologies detected.:\n\n"
        f"{json.dumps(file_structure, indent=4)}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    requirements = response['choices'][0]['message']['content'].strip()
    
    # Print the response for debugging
    print("GPT Requirements Response:")
    print(requirements)

    return requirements

def main():
    with open('file_structure.json', 'r') as f:
        file_structure = json.load(f)
    
    requirements = get_requirements_from_gpt(file_structure)
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)

if __name__ == "__main__":
    main()
