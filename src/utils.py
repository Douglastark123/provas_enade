import os

def file_exists(file: str):
    if not os.path.isfile(file):
        print(f"Error: File {file} does not exist.")
        return False
    return True