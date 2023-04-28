import os
import sys
from code_analysis import extract_code_info
from project_structure import generate_project_structure
import fnmatch

def generate_context(project_path):
    ignore_patterns = ['__pycache__', '*.pyc', '.git', '.gitignore', '.env', '.venv']
    project_structure = generate_project_structure(project_path, ignore_patterns)
    structure_text = "The project has the following structure:\n" + "\n" + (project_structure)

    imports_text = set()
    classes_and_functions_text = []

    for root, dirs, files in os.walk(project_path):
        # Skip the .venv directory
        if '.venv' in dirs:
            dirs.remove('.venv')

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_rel = os.path.relpath(file_path, project_path)

                # Skip items matching the ignore patterns
                if any(fnmatch.fnmatch(file_rel, pattern) for pattern in ignore_patterns):
                    continue

                imports, classes_and_functions = extract_code_info(file_path)
                imports_text.update(imports)
                classes_and_functions_text.extend(classes_and_functions)

    context = f"{structure_text}\n\n"
    context += "The project uses the following libraries:\n" + ", ".join(sorted(filter(None, imports_text))) + "\n\n"
    context += "The project contains the following classes and functions:\n" + "\n".join(classes_and_functions_text) + "\n\n"

    return context


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the project path as a command-line argument.")
        sys.exit(1)

    project_path = sys.argv[1]
    context = generate_context(project_path)
    print(context)
