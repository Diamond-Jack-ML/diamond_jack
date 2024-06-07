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
        "future_features": input("Enter future features: ")
    }
    with open('project_requirements.json', 'w') as f:
        json.dump(project_requirements, f, indent=4)

def create_directories(base_path, structure):
    for directory, sub_structure in structure.items():
        if isinstance(sub_structure, dict):
            directory_path = os.path.join(base_path, directory)
            os.makedirs(directory_path, exist_ok=True)
            with open(os.path.join(directory_path, '.gitkeep'), 'w') as f:
                f.write('')
            if "subdirectories" in sub_structure:
                create_directories(directory_path, sub_structure["subdirectories"])

def create_files(base_path, structure):
    for name, type_or_subdirs in structure.items():
        if type_or_subdirs == "file":
            file_path = os.path.join(base_path, name)
            open(file_path, 'a').close()  # Create empty file

def generate_file_structure():
    with open('file_structure.json', 'r') as f:
        file_structure = json.load(f)
        project_name = file_structure["project_name"]
        directories = file_structure["directories"]

    create_directories(project_name, directories)
    create_files(project_name, directories)

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
