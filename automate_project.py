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
