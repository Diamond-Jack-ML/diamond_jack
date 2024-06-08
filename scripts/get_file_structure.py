import openai
import os
import json

def get_file_structure(tech_stack, description):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    prompt = f"""
    Generate a robust and scalable top-level file structure for a project using {tech_stack} in JSON format. 
    Only include the JSON without additional explanations. The format should be as follows:
    {{
        "projectName": {{
            "directory_or_file_name": {{}},
            "another_directory_or_file_name": {{}}
        }}
    }}
    Here are the additional requirements: {description}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800
    )

    file_structure = response['choices'][0]['message']['content'].strip()
    
    # Print the response for debugging
    print("GPT Response:")
    print(file_structure)
    
    return file_structure

def main():
    tech_stack = input("Enter tech stack (flask, express, django): ")
    description = input("Enter additional project requirements: ")
    
    file_structure = get_file_structure(tech_stack, description)
    
    with open('file_structure.json', 'w') as f:
        f.write(file_structure)

if __name__ == "__main__":
    main()
