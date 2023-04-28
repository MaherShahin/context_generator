import sys
from gpt_query import GPTQuery
from project_analyzer import ProjectAnalyzer
from library_analyzer import LibraryAnalyzer
from documentation_generator import DocumentationGenerator

def generate_context(project_path: str) -> str:
    """
    Generates context for a given project by analyzing its structure, 
    imported libraries, classes, functions, and their descriptions.

    Args:
        project_path (str): The path of the project directory to be analyzed.

    Returns:
        str: The generated context.
    """
    
    project_analyzer = ProjectAnalyzer(project_path)
    structure_text, imports_text, class_hierarchy, docstrings = project_analyzer.analyze()
    documentation_generator = DocumentationGenerator(structure_text, imports_text, class_hierarchy)
    context = documentation_generator.generate_docs()

    return context

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the project path as a command-line argument.")
        sys.exit(1)

    project_path = sys.argv[1]
    context = generate_context(project_path)
    print(context)
