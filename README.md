# CLI Task Automator

`cli-task-automator` is a small Python utility that creates a starter project folder, adds a basic directory layout, writes a couple of default files, and initializes a Git repository with an initial commit.

## What It Does

Running the script creates a new folder with this structure:

```text
project-name/
├── README.md
├── .gitignore
├── src/
└── assets/
```

It also runs the following Git steps inside the new project folder:

1. `git init`
2. `git add .`
3. `git commit -m "Initial commit"`

## Files In This Repository

- `automate_project.py` - the Python script that creates and initializes projects
- `LICENSE` - project license

## Requirements

- Python 3
- Git installed and available on your PATH

## Usage

Run the script from the repository root and pass the name of the project folder you want to create:

```bash
python3 automate_project.py my-new-project
```

Replace `my-new-project` with any folder name you want.

## Behavior

When the script runs successfully, it:

- creates the project directory
- creates `src/` and `assets/` folders
- writes a starter `README.md`
- writes a `.gitignore` with common Python ignores
- initializes a Git repository
- stages the generated files
- makes an initial commit

## Generated Files

The script creates these default files inside the new project:

### `README.md`

Contains a simple project title and a short initialization message.

### `.gitignore`

Includes common Python and local-environment ignores:

```text
__pycache__/
*.pyc
.env
.DS_Store
```

## Error Handling

The script reports errors if Git commands fail or if the filesystem cannot create the requested files and directories.

## Notes

- The script assumes Git is installed and configured well enough to make commits.
- If your Git identity is not configured, the initial commit may fail until `user.name` and `user.email` are set.
- The generated project folder is created next to where the script is run.

## Example

```bash
python3 automate_project.py client-portal
```

This creates a new `client-portal/` folder with the default structure 
