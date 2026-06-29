import argparse
import os
import subprocess
import sys


def create_project(project_name):
    directories = [project_name, os.path.join(
        project_name, 'src'), os.path.join(project_name, 'assets')]
    files = {
        os.path.join(project_name, 'README.md'): f"# {project_name}\nProject initialized automatically.",
        os.path.join(project_name, '.gitignore'): "__pycache__/\n*.pyc\n.env\n.DS_Store"
    }

    try:
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")

        for path, content in files.items():
            with open(path, 'w') as f:
                f.write(content)
            print(f"Created file: {path}")

        print("Initializing git repository...")
        subprocess.run(['git', 'init', cwd= project_name], check=True)
        subprocess.run(['git', 'add', '.'], cwd=project_name, check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'],
                       cwd=project_name, check=True)
        print(
            f"\nSuccessfully created project '{project_name}' with git repository initialized.")

    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}", file=sys.stderr)
    except OSError as e:
        print(f"File System Error: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a standard project structure.")
    parser.add_argument('name', help='Name of the project to create')

    args = parser.parse_args()
    create_project(args.name)
