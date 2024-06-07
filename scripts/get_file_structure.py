import openai
import os
import json

def get_file_structure(tech_stack):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    prompt = f"Generate a robust and scalable file structure for a project using {tech_stack} in JSON format, where subdirectories are nested within their parent directories."
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=300
    )

    file_structure = response.choices[0].text.strip()
    return file_structure

def main():
    tech_stack = input("Enter tech stack (flask, express, django): ")
    file_structure = get_file_structure(tech_stack)
    
    with open('file_structure.json', 'w') as f:
        f.write(file_structure)

if __name__ == "__main__":
    main()
