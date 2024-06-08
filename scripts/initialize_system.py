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

def create_structure(base_path, structure):
    for item, sub_structure in structure.items():
        item_path = os.path.join(base_path, item)
        if isinstance(sub_structure, dict):
            os.makedirs(item_path, exist_ok=True)
            create_structure(item_path, sub_structure)
        else:
            open(item_path, 'a').close()  # Create empty file

def generate_file_structure():
    with open('file_structure.json', 'r') as f:
        file_structure = json.load(f)
        project_name = list(file_structure.keys())[0]  # Dynamically get the project name
        project_files = file_structure[project_name]

    base_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_path, exist_ok=True)
    create_structure(base_path, project_files)

def is_venv_active():
    return os.environ.get('VIRTUAL_ENV') is not None

def create_virtual_environment(base_path):
    if not is_venv_active():
        env_path = os.path.join(base_path, 'env')
        subprocess.run(['python', '-m', 'venv', env_path])

def install_dependencies(base_path):
    if is_venv_active():
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    else:
        activate_script = os.path.join(base_path, 'env', 'Scripts', 'activate.bat')
        requirements_file = os.path.join(base_path, 'requirements.txt')
        subprocess.run(f'call {activate_script} && pip install -r {requirements_file}', shell=True)

def initialize_git_repo(base_path):
    os.system(f'git init {base_path}')
    os.system(f'cd {base_path} && git add . && git commit -m "Initial commit"')

def main():
    get_system_details()
    get_project_requirements()
    generate_file_structure()
    base_path = os.getcwd()
    #create_virtual_environment(base_path)
    install_dependencies(base_path)
    #initialize_git_repo(base_path)

if __name__ == "__main__":
    main()
