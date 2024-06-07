import os
import json
import subprocess

def get_system_details():
    system_details = {
        "system_name": input("Enter system name: "),
        "system_version": input("Enter system version: "),
        "system_description": input("Enter system description: ")
    }
    with open('system_details.json', 'w') as f:
        json.dump(system_details, f, indent=4)

def get_project_requirements():
    project_requirements = {
        "project_name": input("Enter project name: "),
        "tech_stack": input("Enter tech stack: "),
        "future_features": input("Enter future features: ")
    }
    with open('project_requirements.json', 'w') as f:
        json.dump(project_requirements, f, indent=4)

def generate_file_structure():
    directories = [
        "src", "tests", "docs", "logs"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, '.gitkeep'), 'w') as f:
            f.write('')

def create_virtual_environment():
    subprocess.run(['python', '-m', 'venv', 'env'])

def install_dependencies():
    subprocess.run(['env/Scripts/pip', 'install', '-r', 'requirements.txt'])

def initialize_git_repo():
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Initial commit with basic file structure'])

def main():
    get_system_details()
    get_project_requirements()
    generate_file_structure()
    create_virtual_environment()
    install_dependencies()
    initialize_git_repo()

if __name__ == "__main__":
    main()
