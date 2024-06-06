import os

# Define the directory structure with the files to be created
structure = {
    "src/api": ["__init__.py", "task.py", "user.py", ".gitkeep"],
    "src/models": ["__init__.py", "conceptual.py", "logical.py", ".gitkeep"],
    "src/services": ["__init__.py", "gpt_service.py", "jira_service.py", "code_generator.py", "shell_scripting.py", ".gitkeep"],
    "src/utils": ["__init__.py", "config.py", "helpers.py", ".gitkeep"],
    "src": ["main.py", "app.py", ".gitkeep"],
    "tests/test_api": ["test_task.py", "test_user.py", ".gitkeep"],
    "tests/test_models": ["test_conceptual.py", "test_logical.py", ".gitkeep"],
    "tests/test_services": ["test_gpt_service.py", "test_jira_service.py", "test_code_generator.py", "test_shell_scripting.py", ".gitkeep"],
    "tests/test_utils": ["test_config.py", "test_helpers.py", ".gitkeep"],
    "tests": [".gitkeep"],
    "docs/api": ["task.md", "user.md", ".gitkeep"],
    "docs/models": ["conceptual.md", "logical.md", ".gitkeep"],
    "docs/services": ["gpt_service.md", "jira_service.md", "code_generator.md", "shell_scripting.md", ".gitkeep"],
    "docs": ["architecture.md", "setup.md", "usage.md", ".gitkeep"],
}

# Create the files within the existing directories
for directory, files in structure.items():
    for file in files:
        file_path = os.path.join(directory, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

print("Files created successfully.")
