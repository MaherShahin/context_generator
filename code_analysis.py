import jedi

def extract_code_info(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    try:
        script = jedi.Script(content)
        imports = [i.full_name for i in script.get_names(references=True) if i.type == "module"]
        classes_and_functions = [f"{d.type.capitalize()}: {d.full_name}" for d in script.get_names(definitions=True) if d.type in ["class", "function"]]
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        imports = []
        classes_and_functions = []

    return set(imports), classes_and_functions

