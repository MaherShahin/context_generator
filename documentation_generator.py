from gpt_query import GPTQuery

class DocumentationGenerator:

    def __init__(self, project_structure, imports, class_hierarchy):
        """
         Initialize the class. This is called by __init__ and should not be called directly. The project_structure is a dictionary with the structure of the project.
         
         @param project_structure - A dictionary with the structure of the project
         @param imports - A dictionary with the import statements
         @param class_hierarchy - A dictionary with the class hierarchy as
        """
        self.project_structure = project_structure
        self.imports = imports
        self.class_hierarchy = class_hierarchy

    def generate_docs(self):
        """
         Generate documentation for the project. This is a string that can be used to display to the user the information that will be displayed in the documentation page.
         
         
         @return A string that can be displayed to the user the information that will be displayed in the documentation page ( for example to see how to use it
        """
        context = f"{self.project_structure}\n\n"
        context += "The project contains the following classes and functions:\n\n"

        # Generates a string representation of the class hierarchy.
        for class_name, class_data in self.class_hierarchy.items():
            context += f"Class: {class_name}\n"
            context += "-" * 80 + "\n"
            # Generates the context for the functions in the class data.
            if class_data["functions"]:
                context += f"  Functions:\n"
                context += "-" * 80 + "\n"

                # Generates a context for the function
                for function_name, description in class_data["functions"]:
                    context += f"    {function_name}: {description}\n"
                    context += "-" * 80 + "\n"

        context += "\nSummarized Documentation:\n\n"
        descriptions = [
            desc for class_data in self.class_hierarchy.values() 
            for _, desc in class_data["functions"]
        ]
        
        return context
