import os
import fnmatch

def search_files(pattern, root=None):
    if root is None:
        root = os.path.dirname(os.path.abspath(__file__))  # script folder
    matches = []
    for path, dirs, files in os.walk(root):
        for file in fnmatch.filter(files, pattern):
            matches.append(os.path.join(path, file))
    return matches

def fetch_files(root=None):
    if root is None:
        root = os.path.dirname(os.path.abspath(__file__))  # script folder
    all_files = []
    for path, dirs, files in os.walk(root):
        for file in files:
            all_files.append(os.path.join(path, file))
    return all_files

def get_current_dir():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    return script_directory
