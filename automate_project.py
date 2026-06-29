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
