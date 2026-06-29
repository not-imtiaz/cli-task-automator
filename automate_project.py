import argparse
import os
import subprocess
import sys


def create_project(project_name):
    """Creates the standard directory structure and initializes Git."""
    # Define the structure
    directories = [project_name, os.path.join(
        project_name, 'src'), os.path.join(project_name, 'assets')]
    files = {
        os.path.join(project_name, 'README.md'): f"# {project_name}\nProject initialized automatically.",
        os.path.join(project_name, '.gitignore'): "__pycache__/\n*.pyc\n.env\n.DS_Store"
    }

    try:
        # Create directories
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")

        # Create files
        for path, content in files.items():
            with open(path, 'w') as f:
                f.write(content)
            print(f"Created file: {path}")

        # Initialize Git
        print("Initializing Git...")
        subprocess.run(['git', 'init'], cwd=project_name, check=True)
        subprocess.run(['git', 'add', '.'], cwd=project_name, check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'],
                       cwd=project_name, check=True)

        print(f"\nSuccess! Project '{project_name}' is ready.")

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}", file=sys.stderr)
    except OSError as e:
        print(f"File system error: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a standard project structure.")
    parser.add_argument("name", help="Name of the project folder to create")

    args = parser.parse_args()
    create_project(args.name)


if __name__ == "__main__":
    main()
