### Context Generator
The Context Generator is a project that analyzes the structure of a Python project, extracts code information, and generates useful context based on the project's components such as imported libraries, classes, and functions. This generated context can be used for various purposes, such as generating project documentation or providing a high-level overview of the project.

## Project Structure
The project has the following structure:

```
context_generator
├── documentation_generator.py
├── gpt_query.py
├── project_analyzer.py
├── requirements.txt
├── code_analysis.py
├── .env_template
├── library_analyzer.py
├── project_structure.py
└── generate_context.py
```


To use the Context Generator, follow these steps:

1. Clone the project repository:
```
git clone https://github.com/MaherShahin/context_generator
```
2. Navigate to the project directory
```
cd /path/to/context_generator
```

3. Install the required dependencies listed in requirements.txt. You can use the following command to install them:
```
pip install -r requirements.txt
```
4. Create a .env file based on the provided .env_template file. You only need an OPENAI_API_KEY
 
How to Generate Context
To generate context for a specific project, follow these steps:

Ensure you are in the project directory (context_generator).

Run the generate_context.py script with the absolute path of the project directory you want to analyze as an argument. For example:

```
python generate_context.py "/path/to/project"
```
Replace `/path/to/project` with the actual path of the project you want to analyze.

The generated context will be displayed in the console.

License
This project is licensed under the MIT License.