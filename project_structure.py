import os
import fnmatch
from pathlib import Path
from tree_format import format_tree

def generate_project_structure(project_path, ignore_patterns=None):
    if ignore_patterns is None:
        ignore_patterns = ['__pycache__', '*.pyc', '.git', '.gitignore', '.env', '.venv']

    project_path = Path(project_path)

    if not project_path.exists():
        print("The provided project path does not exist. Please check the path and try again.")
        return ""

    def get_children(parent_path):
        children = []
        for item in parent_path.iterdir():
            item_rel = item.relative_to(project_path)

            # Skip items matching the ignore patterns
            if any(fnmatch.fnmatch(item_rel.as_posix(), pattern) for pattern in ignore_patterns):
                continue

            child_node = {'name': str(item_rel)}
            children.append(child_node)

            if item.is_dir():
                child_node['children'] = get_children(item)

        return children

    nodes = [{'name': project_path.name, 'children': get_children(project_path)}]

    if not nodes:
        print("The project directory is empty.")
        return ""

    project_structure = format_tree(nodes[0], lambda n: n['name'], lambda n: n.get('children', []))
    return project_structure
