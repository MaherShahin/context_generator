"""
This module provides functionality for extracting code information 
from a given Python file, including imports, classes, functions, and 
their descriptions.
"""


import jedi

def extract_code_info(file_path: str) -> tuple:
    """
    Extracts code information from a given Python file, including imports, 
    classes, functions, and their descriptions.

    Args:
        file_path (str): The path of the Python file to be analyzed.

    Returns:
        tuple: A tuple containing sets of imports, classes and functions, and descriptions.
    """
    
    with open(file_path, "r") as file:
        content = file.read()

    try:
        script = jedi.Script(content)
        imports = [i.full_name for i in script.get_names(references=True) if i.type == "module"]
        classes_and_functions = [f"{d.type.capitalize()}: {d.full_name}" for d in script.get_names(definitions=True) if d.type in ["class", "function"]]
        descriptions = [d.docstring() for d in script.get_names(definitions=True) if d.type in ["class", "function"]]
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        imports = []
        classes_and_functions = []
        descriptions = []

    return set(imports), classes_and_functions, descriptions

