import os
import json
import subprocess

def capture_commit_state():
    commit_id = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()
    git_log = subprocess.check_output(["git", "log", "--oneline"]).decode()
    shell_session = subprocess.check_output(["history"]).decode()  # Assuming using bash or compatible shell

    logs = {
        "commit_id": commit_id,
        "git_log": git_log,
        "shell_session": shell_session
    }

    with open(os.path.join('logs', f'{commit_id}.json'), 'w') as f:
        json.dump(logs, f, indent=4)

def update_requirements():
    subprocess.run(["env/Scripts/pip", "freeze", ">", "requirements.txt"])

def main():
    capture_commit_state()
    update_requirements()

if __name__ == "__main__":
    main()
