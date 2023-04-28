import os
import fnmatch
from code_analysis import extract_code_info
from project_structure import generate_project_structure


class ProjectAnalyzer:
    def __init__(self, project_path: str, ignore_patterns=None):
        """
         Initialize the class. This is called by __init__ to initialize the class. You can call it yourself as soon as you have a project that is ready to be used.
         
         @param project_path - Path to the project's directory
         @param ignore_patterns - List of patterns to ignore
        """
        self.project_path = project_path
        # Set the ignore patterns to ignore.
        if ignore_patterns is None:
            ignore_patterns = ['__pycache__', '*.pyc', '.git', '.gitignore', '.env', '.venv']
        self.ignore_patterns = ignore_patterns

    def analyze(self):
        """
         Analyze the project and return a string describing the structure. This is a convenience method for use in unit tests.
         
         
         @return The text of the project as a string. import statements. class_hierarchy : A dictionary of classes and functions_text : A string containing the import statements. class_hierarchy : A dictionary of classes and functions
        """
        project_structure = generate_project_structure(self.project_path, self.ignore_patterns)
        structure_text = "The project has the following structure:\n\n" + project_structure

        imports_text = set()
        class_hierarchy = {}
        docstrings = []

        # Recursively walks the project_path and adds the class and functions to the hierarchy.
        for root, dirs, files in os.walk(self.project_path):
            # Remove. venv from the directory if it exists.
            if '.venv' in dirs:
                dirs.remove('.venv')

            # Add all the code files to the hierarchy.
            for file in files:
                # This function is used to create a new class hierarchy for the given file.
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    file_rel = os.path.relpath(file_path, self.project_path)

                    # Return true if any of the ignore patterns in ignore_patterns are present in the file_rel.
                    if any(fnmatch.fnmatch(file_rel, pattern) for pattern in self.ignore_patterns):
                        continue

                    imports, classes_and_functions, descriptions = extract_code_info(file_path)
                    imports_text.update(imports)
                    docstrings.extend(descriptions)

                    # class_or_function is a list of strings containing the class name and function name.
                    for class_or_function, description in zip(classes_and_functions, descriptions):
                        parts = class_or_function.split(":")
                        type = parts[0]
                        name = parts[1].strip()

                        # class_hierarchy. setdefault class_hierarchy name function_name description
                        if type == "Class":
                            class_hierarchy[name] = {"functions": []}
                        elif type == "Function":
                            class_name, function_name = name.split(".")
                            class_data = class_hierarchy.setdefault(class_name, {"functions": []})
                            class_data["functions"].append((function_name, description))

        return structure_text, imports_text, class_hierarchy, docstrings
